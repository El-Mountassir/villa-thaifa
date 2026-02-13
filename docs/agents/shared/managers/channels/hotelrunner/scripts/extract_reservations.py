#!/usr/bin/env python3
"""
HotelRunner Reservations Extractor
Extract daily reservations data from HotelRunner dashboard using browser automation

Author: Craft Agent
Date: 2026-01-24
"""

import subprocess
import json
import logging
from datetime import datetime
from pathlib import Path
import os
import sys

# Configuration
PROFILE_PATH = str(Path.home() / ".hotelrunner-profile")
OUTPUT_DIR = Path(__file__).parent / "data" / "reservations"
LOG_DIR = Path(__file__).parent / "logs"

# Create directories
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Setup logging
log_file = LOG_DIR / f"extract_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def run_browser_command(command: str, timeout: int = 30) -> str:
    """Execute agent-browser command and return output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode != 0:
            logger.error(f"Command failed: {command}")
            logger.error(f"Error: {result.stderr}")
            return None
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        logger.error(f"Command timed out: {command}")
        return None
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        return None


def extract_reservations():
    """Main extraction function"""
    logger.info("=" * 80)
    logger.info("Starting HotelRunner reservations extraction")
    logger.info(f"Profile: {PROFILE_PATH}")
    logger.info(f"Output directory: {OUTPUT_DIR}")

    try:
        # 1. Open browser with persistent profile
        logger.info("Step 1: Opening HotelRunner dashboard...")
        result = run_browser_command(
            f'agent-browser --profile {PROFILE_PATH} open https://villa-thaifa.hotelrunner.com/admin/pms/reservations/all',
            timeout=30
        )

        if result is None:
            logger.error("Failed to open browser")
            return False

        logger.info("✓ Browser opened successfully")

        # 2. Wait for page load
        logger.info("Step 2: Waiting for page load...")
        run_browser_command('sleep 3')

        # 3. Get page title to verify we're logged in
        logger.info("Step 3: Verifying authentication...")
        title = run_browser_command('agent-browser eval "document.title"')

        if title and "login" in title.lower():
            logger.error("Not authenticated! reCAPTCHA may be required.")
            logger.error("Please run: agent-browser --headed --profile ~/.hotelrunner-profile open https://app.hotelrunner.com")
            logger.error("And login manually once to save the session.")
            run_browser_command('agent-browser close')
            return False

        logger.info(f"✓ Authenticated - Page: {title}")

        # 4. Count reservations
        logger.info("Step 4: Counting reservations...")
        count = run_browser_command(
            'agent-browser eval "document.querySelectorAll(\'table tbody tr\').length"'
        )

        if count:
            logger.info(f"✓ Found {count} reservations")
        else:
            logger.warning("Could not count reservations")

        # 5. Extract reservation data
        logger.info("Step 5: Extracting reservation data...")

        # JavaScript to extract all reservations
        extraction_script = """
        Array.from(document.querySelectorAll('table tbody tr'))
            .filter(row => row.querySelectorAll('td').length > 5)
            .map(row => {
                const cells = Array.from(row.querySelectorAll('td')).map(td => td.textContent.trim());
                return {
                    status: cells[0] || '',
                    room: cells[1] || '',
                    channel: cells[2] || '',
                    client_name: cells[3] || '',
                    confirmation_number: cells[4] || '',
                    check_in: cells[5] || '',
                    check_out: cells[6] || '',
                    room_type: cells[7] || '',
                    total: cells[8] || '',
                    payment_total: cells[9] || '',
                    inventory_type: cells[10] || '',
                    confirmation_status: cells[11] || '',
                    booking_date: cells[12] || '',
                    nationality: cells[13] || ''
                };
            })
        """

        # Execute extraction
        reservations_json = run_browser_command(
            f'agent-browser eval "{extraction_script}"',
            timeout=60
        )

        if reservations_json:
            try:
                # Parse JSON
                reservations = json.loads(reservations_json)
                logger.info(f"✓ Successfully extracted {len(reservations)} reservations")

                # Save to file
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                output_file = OUTPUT_DIR / f"reservations_{timestamp}.json"

                output_data = {
                    "extracted_at": datetime.now().isoformat(),
                    "source": "HotelRunner Dashboard - Browser Automation",
                    "count": len(reservations),
                    "reservations": reservations
                }

                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(output_data, f, ensure_ascii=False, indent=2)

                logger.info(f"✓ Data saved to: {output_file}")

                # Also save as "latest" for easy access
                latest_file = OUTPUT_DIR / "latest.json"
                with open(latest_file, 'w', encoding='utf-8') as f:
                    json.dump(output_data, f, ensure_ascii=False, indent=2)

                logger.info(f"✓ Latest copy saved to: {latest_file}")

                # Print summary
                logger.info("\n" + "=" * 80)
                logger.info("EXTRACTION SUMMARY")
                logger.info("=" * 80)
                logger.info(f"Total reservations: {len(reservations)}")
                logger.info(f"Output file: {output_file}")
                logger.info(f"Latest file: {latest_file}")

                # Print sample (first 3 reservations)
                if len(reservations) > 0:
                    logger.info("\nSample reservations:")
                    for i, res in enumerate(reservations[:3], 1):
                        logger.info(f"\n  {i}. {res.get('client_name', 'N/A')}")
                        logger.info(f"     Confirmation: {res.get('confirmation_number', 'N/A')}")
                        logger.info(f"     Check-in: {res.get('check_in', 'N/A')}")
                        logger.info(f"     Check-out: {res.get('check_out', 'N/A')}")
                        logger.info(f"     Status: {res.get('status', 'N/A')}")

                return True

            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON: {e}")
                logger.error(f"Raw output: {reservations_json[:500]}")
                return False
        else:
            logger.error("Failed to extract reservations")
            return False

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return False

    finally:
        # Always close browser
        logger.info("\nClosing browser...")
        run_browser_command('agent-browser close')
        logger.info("✓ Browser closed")
        logger.info("=" * 80)


if __name__ == "__main__":
    logger.info("HotelRunner Reservations Extractor v1.0")
    logger.info(f"Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    success = extract_reservations()

    if success:
        logger.info("\n✅ Extraction completed successfully!")
        sys.exit(0)
    else:
        logger.error("\n❌ Extraction failed!")
        sys.exit(1)
