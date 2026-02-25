# Agent-Browser - Practical Examples

Quick reference for common browser automation tasks.

---

## 🚀 Quick Tests

### Test 1: Basic Navigation

```bash
agent-browser open https://example.com && \
  agent-browser get title && \
  agent-browser close
```

### Test 2: Screenshot

```bash
agent-browser open https://news.ycombinator.com && \
  agent-browser screenshot --full hn.png && \
  agent-browser close
```

### Test 3: Interactive Elements

```bash
agent-browser open https://github.com && \
  agent-browser snapshot -i -c && \
  agent-browser close
```

---

## 🔍 Web Scraping

### Extract Article Titles

```bash
agent-browser open https://news.ycombinator.com
agent-browser eval "Array.from(document.querySelectorAll('.titleline > a')).map(a => a.textContent).slice(0, 10)"
agent-browser close
```

### Get All Links

```bash
agent-browser open https://example.com
agent-browser eval "Array.from(document.querySelectorAll('a')).map(a => ({text: a.textContent, href: a.href}))"
agent-browser close
```

### Extract Prices from E-commerce

```bash
agent-browser open https://shop.example.com/products
agent-browser snapshot -i --json > products.json
agent-browser eval "Array.from(document.querySelectorAll('.price')).map(p => p.textContent)"
agent-browser close
```

---

## 📝 Form Automation

### Google Search

```bash
agent-browser open https://www.google.com
agent-browser fill "textarea[name='q']" "Claude AI"
agent-browser press Enter
sleep 3
agent-browser get title
agent-browser close
```

### Contact Form

```bash
agent-browser open https://example.com/contact
agent-browser snapshot -i -c
# Identify form fields with refs
agent-browser fill @e3 "John Doe"
agent-browser fill @e4 "john@example.com"
agent-browser fill @e5 "This is my message"
agent-browser click @e6  # Submit button
agent-browser wait 3000
agent-browser screenshot success.png
agent-browser close
```

### Newsletter Signup

```bash
agent-browser open https://blog.example.com
agent-browser fill "input[type='email']" "user@example.com"
agent-browser click "button[type='submit']"
agent-browser wait ".success-message"
agent-browser get text ".success-message"
agent-browser close
```

---

## 🔐 Authentication & Sessions

### Login Once, Reuse Session

```bash
# First time - login
agent-browser --profile ~/.profiles/twitter open https://twitter.com
agent-browser snapshot -i
agent-browser fill "#username" "myusername"
agent-browser fill "#password" "mypassword"
agent-browser click "button[type='submit']"
agent-browser wait 5000
agent-browser close

# Next time - already logged in!
agent-browser --profile ~/.profiles/twitter open https://twitter.com
agent-browser get title
agent-browser close
```

### Multiple Accounts (Isolated Sessions)

```bash
# Account 1
agent-browser --session acc1 --profile ~/.profiles/acc1 open https://site.com

# Account 2 (different session)
agent-browser --session acc2 --profile ~/.profiles/acc2 open https://site.com

# Both can run simultaneously
```

---

## 📸 Screenshots & Documentation

### Full Page Screenshot

```bash
agent-browser open https://tailwindcss.com
agent-browser screenshot --full tailwind-docs.png
agent-browser close
```

### Multiple Screenshots (Monitoring)

```bash
for i in {1..5}; do
  agent-browser --session monitor open https://status.example.com
  agent-browser screenshot --full "status-$i.png"
  sleep 60  # Wait 1 minute
done
agent-browser --session monitor close
```

### Export to PDF

```bash
agent-browser open https://en.wikipedia.org/wiki/Artificial_intelligence
agent-browser pdf wikipedia-ai.pdf
agent-browser close
```

---

## 🎯 Interactive Navigation

### Click Through Menu

```bash
agent-browser open https://example.com
agent-browser snapshot -i -c
agent-browser click @e_menu  # Click menu
agent-browser wait 1000
agent-browser snapshot -i -c  # Get submenu items
agent-browser click @e_products
agent-browser get url
agent-browser close
```

### Pagination

```bash
agent-browser open https://example.com/products
for i in {1..5}; do
  agent-browser snapshot -i --json > "page-$i.json"
  agent-browser click "a.next-page"
  agent-browser wait 2000
done
agent-browser close
```

---

## 🧪 Testing & Validation

### Check Element Visibility

```bash
agent-browser open https://example.com
agent-browser is visible "button.submit"
agent-browser is enabled "input#email"
agent-browser close
```

### Verify Page Content

```bash
agent-browser open https://example.com
TITLE=$(agent-browser get title)
if [[ "$TITLE" == "Expected Title" ]]; then
  echo "✅ Page loaded correctly"
else
  echo "❌ Page title mismatch"
fi
agent-browser close
```

### Monitor Page Changes

```bash
# Initial state
agent-browser open https://example.com
agent-browser eval "document.body.innerHTML" > before.html

# Wait and check again
sleep 300  # 5 minutes
agent-browser eval "document.body.innerHTML" > after.html
diff before.html after.html
agent-browser close
```

---

## 📊 Data Collection

### Scrape Table Data

```bash
agent-browser open https://example.com/table
agent-browser eval "
  Array.from(document.querySelectorAll('table tr')).map(tr =>
    Array.from(tr.querySelectorAll('td')).map(td => td.textContent)
  )
" --json > table-data.json
agent-browser close
```

### Extract Metadata

```bash
agent-browser open https://example.com
agent-browser eval "{
  title: document.title,
  description: document.querySelector('meta[name=\"description\"]')?.content,
  keywords: document.querySelector('meta[name=\"keywords\"]')?.content,
  ogImage: document.querySelector('meta[property=\"og:image\"]')?.content
}"
agent-browser close
```

### Get All Images

```bash
agent-browser open https://example.com/gallery
agent-browser eval "Array.from(document.querySelectorAll('img')).map(img => ({
  src: img.src,
  alt: img.alt,
  width: img.naturalWidth,
  height: img.naturalHeight
}))" --json > images.json
agent-browser close
```

---

## 🔄 Advanced Workflows

### Complete Research Workflow

```bash
#!/bin/bash

# Open Hacker News
agent-browser open https://news.ycombinator.com

# Get top 5 articles
agent-browser snapshot -i -c | grep "link.*ref=" | head -5 > articles.txt

# Click first article
agent-browser click @e12
sleep 2

# Capture article
agent-browser screenshot --full article.png
agent-browser pdf article.pdf
agent-browser eval "document.querySelector('article')?.textContent || document.body.textContent" > article.txt

# Go back and continue
agent-browser back
sleep 1

# Close when done
agent-browser close
```

### E-commerce Price Monitor

```bash
#!/bin/bash

URL="https://shop.example.com/product/123"
PROFILE="~/.profiles/shop"

agent-browser --profile "$PROFILE" open "$URL"
PRICE=$(agent-browser get text ".price")
DATE=$(date +%Y-%m-%d)

echo "$DATE,$PRICE" >> price-history.csv
agent-browser close

# Run this daily via cron
```

### Automated Testing

```bash
#!/bin/bash

agent-browser open https://myapp.test
agent-browser fill "#username" "testuser"
agent-browser fill "#password" "testpass"
agent-browser click "button[type='submit']"

if agent-browser is visible ".dashboard"; then
  echo "✅ Login successful"
  agent-browser screenshot dashboard.png
else
  echo "❌ Login failed"
  agent-browser screenshot error.png
  exit 1
fi

agent-browser close
```

---

## 🎨 Creative Uses

### Generate Social Media Previews

```bash
agent-browser open https://myblog.com/post/123
agent-browser set viewport 1200 630  # Twitter card size
agent-browser screenshot --full twitter-card.png
agent-browser close
```

### Archive Website State

```bash
DATE=$(date +%Y%m%d)
agent-browser open https://important-site.com
agent-browser screenshot --full "archive-$DATE.png"
agent-browser pdf "archive-$DATE.pdf"
agent-browser eval "document.documentElement.outerHTML" > "archive-$DATE.html"
agent-browser close
```

### Compare Two Sites

```bash
agent-browser --session site1 open https://site1.com
agent-browser --session site1 screenshot site1.png

agent-browser --session site2 open https://site2.com
agent-browser --session site2 screenshot site2.png

agent-browser --session site1 close
agent-browser --session site2 close

# Compare screenshots
compare site1.png site2.png diff.png
```

---

## 💡 Pro Tips

### Chain Multiple Operations

```bash
agent-browser open URL && \
  agent-browser snapshot -i -c && \
  agent-browser screenshot output.png && \
  agent-browser pdf output.pdf && \
  agent-browser close
```

### Use JSON Output for Processing

```bash
agent-browser open https://api.github.com
DATA=$(agent-browser eval "JSON.parse(document.body.textContent)" --json)
echo "$DATA" | jq '.current_user_url'
agent-browser close
```

### Persistent Monitoring Session

```bash
# Open once
agent-browser --session monitor open https://status.example.com

# Check periodically (don't close)
while true; do
  agent-browser --session monitor screenshot "status-$(date +%s).png"
  sleep 300  # 5 minutes
done
```

---

**Last Updated**: January 24, 2026
