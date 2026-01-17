<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sync Investigation Report v1.2 | Villa Thaifa</title>
  <style>
    :root {
      --bg-primary: #0D1117;
      --bg-secondary: #161B22;
      --bg-tertiary: #21262D;
      --text-primary: #C9D1D9;
      --text-secondary: #8B949E;
      --text-muted: #484F58;
      --border-color: #30363D;
      --accent-blue: #58A6FF;
      --accent-green: #3FB950;
      --accent-purple: #A371F7;
      --accent-orange: #D29922;
      --accent-red: #F85149;
      --accent-yellow: #F0E68C;
      --shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      --radius-sm: 6px;
      --radius-md: 8px;
      --radius-lg: 12px;
    }

    [data-theme="light"] {
      --bg-primary: #FFFFFF;
      --bg-secondary: #F6F8FA;
      --bg-tertiary: #EAEEF2;
      --text-primary: #24292F;
      --text-secondary: #57606A;
      --text-muted: #8C959F;
      --border-color: #D0D7DE;
      --accent-blue: #0969DA;
      --accent-green: #1A7F37;
      --accent-purple: #8250DF;
      --accent-orange: #BF8700;
      --accent-red: #CF222E;
      --accent-yellow: #9A8700;
      --shadow: 0 8px 24px rgba(140, 149, 159, 0.2);
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html {
      font-size: 16px;
      scroll-behavior: smooth;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
      background: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      min-height: 100vh;
    }

    .app {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    /* Header */
    .header {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-content {
      max-width: 900px;
      margin: 0 auto;
      padding: 1rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--accent-blue);
      font-weight: 600;
    }

    .logo-icon {
      font-size: 1.5rem;
    }

    .logo-text {
      font-size: 1rem;
    }

    .header-title {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--text-primary);
    }

    .header-actions {
      display: flex;
      gap: 0.5rem;
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.625rem 1.25rem;
      border: none;
      border-radius: var(--radius-md);
      font-family: inherit;
      font-size: 0.9375rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    .btn-primary {
      background: var(--accent-blue);
      color: white;
    }

    .btn-primary:hover:not(:disabled) {
      filter: brightness(1.1);
    }

    .btn-secondary {
      background: var(--bg-tertiary);
      color: var(--text-primary);
    }

    .btn-secondary:hover:not(:disabled) {
      background: var(--border-color);
    }

    .btn-icon {
      width: 36px;
      height: 36px;
      padding: 0;
      background: transparent;
      color: var(--text-secondary);
    }

    .btn-icon:hover {
      background: var(--bg-tertiary);
      color: var(--text-primary);
    }

    [data-theme="dark"] .icon-sun { display: inline; }
    [data-theme="dark"] .icon-moon { display: none; }
    [data-theme="light"] .icon-sun { display: none; }
    [data-theme="light"] .icon-moon { display: inline; }

    /* Navigation */
    .nav {
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--border-color);
      padding: 0.75rem 2rem;
      overflow-x: auto;
    }

    .nav-track {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      gap: 0.25rem;
      flex-wrap: wrap;
    }

    .nav-item {
      padding: 0.5rem 1rem;
      border-radius: var(--radius-md);
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .nav-item:hover {
      background: var(--bg-tertiary);
      color: var(--text-primary);
    }

    /* Main Content */
    .main {
      flex: 1;
      padding: 2rem;
    }

    .content {
      max-width: 900px;
      margin: 0 auto;
    }

    /* Sections */
    .section {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 1.5rem;
    }

    .section-header {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1.5rem;
      cursor: pointer;
    }

    .section-icon {
      font-size: 1.5rem;
      color: var(--accent-blue);
      flex-shrink: 0;
    }

    .section-title {
      font-size: 1.375rem;
      margin-bottom: 0.25rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .section-subtitle {
      color: var(--text-secondary);
      font-size: 0.875rem;
    }

    .section-content {
      transition: all 0.3s ease;
    }

    .section.collapsed .section-content {
      display: none;
    }

    .section.collapsed .collapse-icon {
      transform: rotate(-90deg);
    }

    .collapse-icon {
      font-size: 0.75rem;
      color: var(--text-muted);
      transition: transform 0.2s ease;
    }

    /* Badge */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.375rem;
      padding: 0.25rem 0.75rem;
      border-radius: 2rem;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.025em;
    }

    .badge-critical {
      background: rgba(248, 81, 73, 0.15);
      color: var(--accent-red);
      border: 1px solid var(--accent-red);
    }

    .badge-success {
      background: rgba(63, 185, 80, 0.15);
      color: var(--accent-green);
      border: 1px solid var(--accent-green);
    }

    .badge-warning {
      background: rgba(210, 153, 34, 0.15);
      color: var(--accent-orange);
      border: 1px solid var(--accent-orange);
    }

    .badge-info {
      background: rgba(88, 166, 255, 0.15);
      color: var(--accent-blue);
      border: 1px solid var(--accent-blue);
    }

    /* Meta Info */
    .meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 1.5rem;
      padding: 1rem;
      background: var(--bg-tertiary);
      border-radius: var(--radius-md);
    }

    .meta-item {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .meta-label {
      font-size: 0.75rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .meta-value {
      font-weight: 600;
      color: var(--text-primary);
    }

    /* Summary Cards */
    .summary-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
    }

    .summary-card {
      background: var(--bg-tertiary);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      border-left: 4px solid var(--accent-blue);
    }

    .summary-card.critical {
      border-left-color: var(--accent-red);
    }

    .summary-card.warning {
      border-left-color: var(--accent-orange);
    }

    .summary-card.success {
      border-left-color: var(--accent-green);
    }

    .summary-card h4 {
      font-size: 0.875rem;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.025em;
      margin-bottom: 0.5rem;
    }

    .summary-card p {
      color: var(--text-primary);
      font-size: 0.9375rem;
    }

    /* Discovery Box */
    .discovery-box {
      background: rgba(210, 153, 34, 0.1);
      border: 1px solid var(--accent-orange);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin: 1.5rem 0;
    }

    .discovery-box h4 {
      color: var(--accent-orange);
      font-size: 1rem;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .discovery-box p {
      color: var(--text-secondary);
      margin-bottom: 0.75rem;
    }

    .recommendation-box {
      background: rgba(88, 166, 255, 0.1);
      border: 1px solid var(--accent-blue);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-top: 1rem;
    }

    .recommendation-box h5 {
      color: var(--accent-blue);
      font-size: 0.875rem;
      margin-bottom: 0.5rem;
    }

    .recommendation-box p {
      color: var(--text-secondary);
      font-size: 0.9375rem;
      margin: 0;
    }

    /* Caveat Box (NEW) */
    .caveat-box {
      background: rgba(163, 113, 247, 0.1);
      border: 1px solid var(--accent-purple);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-top: 1rem;
    }

    .caveat-box h5 {
      color: var(--accent-purple);
      font-size: 0.875rem;
      margin-bottom: 0.5rem;
    }

    .caveat-box p {
      color: var(--text-secondary);
      font-size: 0.9375rem;
      margin: 0;
    }

    /* Mitigation Box (NEW) */
    .mitigation-box {
      background: rgba(63, 185, 80, 0.1);
      border: 1px solid var(--accent-green);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-top: 1rem;
    }

    .mitigation-box h5 {
      color: var(--accent-green);
      font-size: 0.875rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .mitigation-box p {
      color: var(--text-secondary);
      font-size: 0.9375rem;
      margin: 0;
    }

    /* Timeline */
    .timeline {
      position: relative;
      padding-left: 2rem;
    }

    .timeline::before {
      content: '';
      position: absolute;
      left: 0.5rem;
      top: 0;
      bottom: 0;
      width: 2px;
      background: var(--border-color);
    }

    .timeline-item {
      position: relative;
      padding-bottom: 1.5rem;
    }

    .timeline-item:last-child {
      padding-bottom: 0;
    }

    .timeline-marker {
      position: absolute;
      left: -1.625rem;
      top: 0.25rem;
      width: 1.25rem;
      height: 1.25rem;
      border-radius: 50%;
      background: var(--bg-secondary);
      border: 2px solid var(--accent-green);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.625rem;
      color: var(--accent-green);
    }

    .timeline-title {
      font-weight: 600;
      margin-bottom: 0.25rem;
    }

    .timeline-subtitle {
      color: var(--text-secondary);
      font-size: 0.875rem;
    }

    /* Tables */
    .table-container {
      overflow-x: auto;
      margin: 1rem 0;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9375rem;
    }

    th, td {
      padding: 0.75rem 1rem;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }

    th {
      background: var(--bg-tertiary);
      font-weight: 600;
      font-size: 0.8125rem;
      text-transform: uppercase;
      letter-spacing: 0.025em;
      color: var(--text-secondary);
    }

    tr:hover td {
      background: var(--bg-tertiary);
    }

    .status-check {
      color: var(--accent-green);
      font-weight: bold;
    }

    .status-cross {
      color: var(--accent-red);
      font-weight: bold;
    }

    .status-done {
      color: var(--accent-green);
      font-weight: 600;
    }

    .status-pending {
      color: var(--accent-orange);
      font-weight: 600;
    }

    .status-warning {
      color: var(--accent-orange);
      font-weight: 600;
    }

    .discrepancy {
      color: var(--accent-red);
      font-weight: 600;
    }

    .correct {
      color: var(--accent-green);
    }

    /* Action Items */
    .action-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .action-item {
      display: flex;
      gap: 0.75rem;
      padding: 1rem;
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .action-item:hover {
      border-color: var(--accent-blue);
    }

    .action-item.checked {
      border-color: var(--accent-green);
      background: rgba(63, 185, 80, 0.1);
    }

    .action-checkbox {
      flex-shrink: 0;
      width: 20px;
      height: 20px;
      border: 2px solid var(--border-color);
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
      color: transparent;
      font-size: 0.75rem;
    }

    .action-item.checked .action-checkbox {
      background: var(--accent-green);
      border-color: var(--accent-green);
      color: white;
    }

    .action-content {
      flex: 1;
    }

    .action-priority {
      display: inline-block;
      padding: 0.125rem 0.5rem;
      border-radius: var(--radius-sm);
      font-size: 0.6875rem;
      font-weight: 600;
      margin-right: 0.5rem;
    }

    .priority-p0 {
      background: rgba(248, 81, 73, 0.2);
      color: var(--accent-red);
    }

    .priority-p1 {
      background: rgba(210, 153, 34, 0.2);
      color: var(--accent-orange);
    }

    .priority-p2 {
      background: rgba(88, 166, 255, 0.2);
      color: var(--accent-blue);
    }

    .action-label {
      font-weight: 600;
      margin-bottom: 0.25rem;
    }

    .action-item.checked .action-label {
      text-decoration: line-through;
      opacity: 0.7;
    }

    .action-owner {
      font-size: 0.8125rem;
      color: var(--text-muted);
    }

    .action-result {
      font-size: 0.8125rem;
      color: var(--accent-green);
      margin-top: 0.25rem;
    }

    .action-status {
      font-size: 0.8125rem;
      color: var(--accent-orange);
      margin-top: 0.25rem;
    }

    .action-group-title {
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-secondary);
      margin-top: 1.5rem;
      margin-bottom: 0.75rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
    }

    .action-group-title:first-child {
      margin-top: 0;
    }

    /* Code Block */
    .code-block {
      position: relative;
      background: var(--bg-primary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1rem;
      font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
      font-size: 0.8125rem;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }

    .code-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .code-title {
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--text-secondary);
    }

    .copy-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.375rem;
      padding: 0.375rem 0.75rem;
      background: var(--bg-tertiary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      color: var(--text-secondary);
      font-size: 0.75rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .copy-btn:hover {
      background: var(--border-color);
      color: var(--text-primary);
    }

    .copy-btn.copied {
      background: var(--accent-green);
      border-color: var(--accent-green);
      color: white;
    }

    /* Info Box */
    .info-box {
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      margin: 1rem 0;
      border-left: 4px solid;
    }

    .info-box.hypothesis {
      background: rgba(163, 113, 247, 0.1);
      border-color: var(--accent-purple);
    }

    .info-box.note {
      background: rgba(88, 166, 255, 0.1);
      border-color: var(--accent-blue);
    }

    .info-box-title {
      font-weight: 600;
      margin-bottom: 0.5rem;
      color: var(--accent-purple);
    }

    .info-box.note .info-box-title {
      color: var(--accent-blue);
    }

    .info-box blockquote {
      font-style: italic;
      color: var(--text-secondary);
      margin: 0.5rem 0;
      padding-left: 1rem;
      border-left: 2px solid var(--border-color);
    }

    /* Root Cause Visual */
    .root-cause-visual {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.5rem 0;
    }

    .flow-item {
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 1rem;
      background: var(--bg-tertiary);
      border-radius: var(--radius-md);
    }

    .flow-icon {
      font-size: 1.5rem;
      flex-shrink: 0;
    }

    .flow-arrow {
      font-size: 1.25rem;
      color: var(--text-muted);
    }

    .flow-status {
      margin-left: auto;
      font-weight: 600;
    }

    .flow-status.working {
      color: var(--accent-green);
    }

    .flow-status.broken {
      color: var(--accent-red);
    }

    /* Update Log */
    .update-log {
      margin-top: 1rem;
    }

    .update-log table {
      font-size: 0.875rem;
    }

    .update-log tr.current {
      background: rgba(63, 185, 80, 0.1);
    }

    /* Footer */
    .footer {
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-color);
      padding: 0.75rem 2rem;
    }

    .footer-content {
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8125rem;
      color: var(--text-muted);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .header-content {
        padding: 0.75rem 1rem;
      }

      .header-title {
        font-size: 1rem;
      }

      .logo-text {
        display: none;
      }

      .nav {
        padding: 0.5rem 1rem;
      }

      .main {
        padding: 1rem;
      }

      .section {
        padding: 1.25rem;
      }

      .section-title {
        font-size: 1.125rem;
      }

      .meta-grid {
        grid-template-columns: 1fr;
      }

      .summary-cards {
        grid-template-columns: 1fr;
      }

      .footer-content {
        flex-direction: column;
        gap: 0.5rem;
        text-align: center;
      }

      .table-container {
        margin: 1rem -1.25rem;
        padding: 0 1.25rem;
      }
    }

    /* Print Styles */
    @media print {
      .header {
        position: static;
      }

      .nav,
      .btn-icon,
      .copy-btn {
        display: none;
      }

      .section {
        break-inside: avoid;
        border: 1px solid #ccc;
        box-shadow: none;
      }

      .section.collapsed .section-content {
        display: block;
      }

      .action-item {
        break-inside: avoid;
      }

      body {
        background: white;
        color: black;
      }

      .section {
        background: white;
      }
    }
  </style>
</head>
<body>
  <div class="app">
    <header class="header">
      <div class="header-content">
        <div class="logo">
          <span class="logo-icon">&#127968;</span>
          <span class="logo-text">Villa Thaifa</span>
        </div>
        <h1 class="header-title">Sync Investigation Report v1.2</h1>
        <div class="header-actions">
          <button id="theme-toggle" class="btn btn-icon" title="Toggle theme">
            <span class="icon-sun">&#9728;</span>
            <span class="icon-moon">&#9790;</span>
          </button>
          <button id="print-btn" class="btn btn-icon" title="Print report">
            &#128424;
          </button>
        </div>
      </div>
    </header>

    <nav class="nav">
      <div class="nav-track">
        <a href="#p0-actions" class="nav-item">P0 Actions</a>
        <a href="#executive-summary" class="nav-item">Summary</a>
        <a href="#connectivity" class="nav-item">Connectivity</a>
        <a href="#timeline" class="nav-item">Timeline</a>
        <a href="#root-cause" class="nav-item">Root Cause</a>
        <a href="#evidence" class="nav-item">Evidence</a>
        <a href="#actions" class="nav-item">Actions</a>
        <a href="#support-ticket" class="nav-item">Support Ticket</a>
        <a href="#update-log" class="nav-item">Updates</a>
      </div>
    </nav>

    <main class="main">
      <div class="content">
        <!-- P0 Actions Completed -->
        <section class="section" id="p0-actions">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#9989;</span>
            <div>
              <h2 class="section-title">
                P0 Actions Completed (2025-12-29)
                <span class="badge badge-success">DONE</span>
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Critical actions executed to mitigate double-booking risk</p>
            </div>
          </div>
          <div class="section-content">
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Action</th>
                    <th>Status</th>
                    <th>Result</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Block Dec 31 - Jan 2 on Booking.com</td>
                    <td><span class="status-done">DONE</span></td>
                    <td>"Chambre Double Superieur 4;5" closed via Open/Close Rooms wizard</td>
                  </tr>
                  <tr>
                    <td>Check HotelRunner "Sync Availability" setting</td>
                    <td><span class="status-done">DONE</span></td>
                    <td>No explicit toggle found - see findings below</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="discovery-box">
              <h4>&#128161; Key Discovery: "Allocation Type" Setting</h4>
              <p>In HotelRunner &#8594; Channels &#8594; Booking.com &#8594; Room type mapping &#8594; <strong>Advanced settings</strong>:</p>
              <div class="table-container">
                <table>
                  <thead>
                    <tr>
                      <th>Setting</th>
                      <th>Current Value</th>
                      <th>Issue</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Allocation Type</strong></td>
                      <td><strong>"No changes"</strong></td>
                      <td><span class="status-warning">&#9888; Likely prevents availability push!</span></td>
                    </tr>
                    <tr>
                      <td>Base allotment</td>
                      <td>(empty)</td>
                      <td>Not configured</td>
                    </tr>
                    <tr>
                      <td>Last imported</td>
                      <td>Dec 08, 2025</td>
                      <td><span class="status-warning">3 weeks stale</span></td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div class="recommendation-box">
                <h5>&#128204; Recommendation</h5>
                <p>Change "Allocation Type" from "No changes" to an active sync mode. Contact HotelRunner support for guidance on correct setting.</p>
              </div>
              <div class="caveat-box">
                <h5>&#9888; Note</h5>
                <p>We could not view the dropdown options for "Allocation Type" during this investigation. HotelRunner support should advise on the correct setting value.</p>
              </div>
            </div>
          </div>
        </section>

        <!-- Executive Summary -->
        <section class="section" id="executive-summary">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128203;</span>
            <div>
              <h2 class="section-title">
                Executive Summary
                <span class="badge badge-critical">Critical (mitigated)</span>
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">HotelRunner - Booking.com Sync Failure Investigation</p>
            </div>
          </div>
          <div class="section-content">
            <div class="meta-grid">
              <div class="meta-item">
                <span class="meta-label">Date</span>
                <span class="meta-value">2025-12-29</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">Investigator</span>
                <span class="meta-value">Claude (AI Agent)</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">Validated By</span>
                <span class="meta-value">Omar El Mountassir</span>
              </div>
              <div class="meta-item">
                <span class="meta-label">Status</span>
                <span class="meta-value" style="color: var(--accent-green);">P0 ACTIONS COMPLETED</span>
              </div>
            </div>

            <div class="summary-cards">
              <div class="summary-card critical">
                <h4>Problem</h4>
                <p>Internal/direct reservations created on HotelRunner do NOT sync to Booking.com, leaving dates available for double-booking.</p>
              </div>
              <div class="summary-card">
                <h4>Root Cause</h4>
                <p>The Two-Way XML sync only processes Booking.com-originating reservations. Internal ("Online") reservations do not trigger availability updates.</p>
              </div>
              <div class="summary-card success">
                <h4>Mitigation</h4>
                <p>Affected dates (Dec 31 - Jan 2) manually blocked on Booking.com. "Allocation Type" setting identified as likely culprit.</p>
              </div>
            </div>

            <div class="info-box note" style="margin-top: 1.5rem;">
              <div class="info-box-title">Affected Reservations (Confirmed)</div>
              <ul style="margin: 0.5rem 0 0 1.5rem; color: var(--text-secondary);">
                <li><strong>Sabah Gouram</strong>: Dec 31, 2025 - Jan 3, 2026 (Room 4)</li>
                <li><strong>Famille Benchekroune</strong>: Dec 31, 2025 - Jan 2, 2026 (Room 5)</li>
              </ul>
            </div>
          </div>
        </section>

        <!-- HotelRunner Connectivity Status (NEW) -->
        <section class="section" id="connectivity">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128279;</span>
            <div>
              <h2 class="section-title">
                HotelRunner Connectivity Status
                <span class="badge badge-success">ALL ACTIVE</span>
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">All services show active connection to Booking.com (2025-12-29)</p>
            </div>
          </div>
          <div class="section-content">
            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Service</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Connection status</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Content</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Guest Reviews</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Messaging</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Performance Data And Insights</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Photos</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr style="background: rgba(63, 185, 80, 0.1);">
                    <td><strong>Rate and Availability</strong></td>
                    <td><span class="status-check"><strong>&#10003; Connection is active</strong></span></td>
                  </tr>
                  <tr>
                    <td>Reporting</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                  <tr>
                    <td>Reservations</td>
                    <td><span class="status-check">&#10003; Connection is active</span></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="info-box note">
              <div class="info-box-title">&#128161; Implication</div>
              <p style="margin: 0;">The capability to sync availability <strong>EXISTS</strong>. The issue is likely <strong>configuration</strong> (Allocation Type setting), not a missing feature.</p>
            </div>
          </div>
        </section>

        <!-- Investigation Timeline -->
        <section class="section" id="timeline">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128337;</span>
            <div>
              <h2 class="section-title">
                Investigation Timeline
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Phases completed during the investigation</p>
            </div>
          </div>
          <div class="section-content">
            <div class="timeline">
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 1: Channel Connection Status</div>
                <div class="timeline-subtitle">Booking.com active, Two-Way XML, Last sync: Dec 29, 2025 02:29</div>
              </div>
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 2: Room Mapping Audit</div>
                <div class="timeline-subtitle">All 8 room types properly mapped, no Read Only flags</div>
              </div>
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 3: Transaction Logs Review</div>
                <div class="timeline-subtitle">3,588 transactions, 100% success rate, 0 failures</div>
              </div>
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 4-5: Calendar Comparison</div>
                <div class="timeline-subtitle">Discrepancy identified between HotelRunner and Booking.com availability</div>
              </div>
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 6: Root Cause Analysis</div>
                <div class="timeline-subtitle">Internal reservations not triggering availability updates</div>
              </div>
              <div class="timeline-item">
                <div class="timeline-marker">&#10003;</div>
                <div class="timeline-title">Phase 7: P0 Actions Executed</div>
                <div class="timeline-subtitle">Dates blocked on Booking.com, "Allocation Type" setting discovered</div>
              </div>
            </div>
          </div>
        </section>

        <!-- Root Cause Analysis -->
        <section class="section" id="root-cause">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128269;</span>
            <div>
              <h2 class="section-title">
                Root Cause Analysis
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Understanding the sync behavior</p>
            </div>
          </div>
          <div class="section-content">
            <h3 style="font-size: 1rem; margin-bottom: 1rem; color: var(--text-secondary);">Confirmed Sync Behavior</h3>

            <div class="root-cause-visual">
              <div class="flow-item">
                <span class="flow-icon">&#127760;</span>
                <div>
                  <strong>Booking.com to HotelRunner</strong>
                  <div style="font-size: 0.875rem; color: var(--text-secondary);">Reservations from Booking.com appear in HotelRunner</div>
                </div>
                <span class="flow-arrow">&#8594;</span>
                <span class="flow-status working">&#10003; Working</span>
              </div>

              <div class="flow-item">
                <span class="flow-icon">&#128187;</span>
                <div>
                  <strong>HotelRunner to Booking.com (Booking.com reservations)</strong>
                  <div style="font-size: 0.875rem; color: var(--text-secondary);">Net booked shows correctly for Dec 29-30</div>
                </div>
                <span class="flow-arrow">&#8594;</span>
                <span class="flow-status working">&#10003; Working</span>
              </div>

              <div class="flow-item" style="border: 2px solid var(--accent-red);">
                <span class="flow-icon">&#128187;</span>
                <div>
                  <strong>HotelRunner to Booking.com (Internal reservations)</strong>
                  <div style="font-size: 0.875rem; color: var(--text-secondary);">Manual/internal reservations do not update Booking.com availability</div>
                </div>
                <span class="flow-arrow">&#8594;</span>
                <span class="flow-status broken">&#10007; NOT SYNCING</span>
              </div>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Hypothesis (Updated 2025-12-29)</h3>
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">The XML connection is configured for <strong>reservation synchronization</strong> (pulling Booking.com reservations) but NOT for <strong>availability push</strong> (sending internal reservations to block Booking.com calendar).</p>

            <div class="discovery-box">
              <h4>&#128161; NEW FINDING</h4>
              <p>The "Allocation Type" setting in Room type mapping &#8594; Advanced settings is set to <strong>"No changes"</strong>, which likely means HotelRunner does NOT push availability updates to Booking.com for this room type.</p>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Connection Type Analysis</h3>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Connection Type</th>
                    <th>Description</th>
                    <th>Villa Thaifa Status</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>One-Way Pull</td>
                    <td>Only receives reservations from OTAs</td>
                    <td class="status-cross">&#10007;</td>
                  </tr>
                  <tr>
                    <td>Two-Way Reservation</td>
                    <td>Sends/receives reservations but not manual availability blocks</td>
                    <td class="status-check">&#10003; Current</td>
                  </tr>
                  <tr>
                    <td>Full Two-Way</td>
                    <td>Sends availability updates for ALL reservations (including internal)</td>
                    <td class="status-cross">&#10007; Required</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Additional Evidence</h3>
            <ul style="margin: 0.5rem 0 0 1.5rem; color: var(--text-secondary);">
              <li>Last import from Booking.com: December 08, 2025 (3 weeks ago)</li>
              <li>"Update room availabilities after importing the reservations" checkbox exists but only applies to IMPORT, not EXPORT</li>
            </ul>

            <div class="info-box hypothesis" style="margin-top: 1.5rem;">
              <div class="info-box-title">Omar's Hypothesis</div>
              <blockquote>"Je pense que c'est a cause du fait que le mapping des chambres sur booking doit etre modifier pour devenir en chambres et pas groupe par type."</blockquote>
              <p style="margin-top: 0.75rem;"><strong>Assessment:</strong> This hypothesis has merit. Currently Booking.com shows "Chambre Double Superieur <strong>4 ; 5</strong>" as a single room type, while HotelRunner manages Room 4 and Room 5 as individual rooms.</p>
              <p style="margin-top: 0.5rem;">However, this doesn't fully explain why the room-type availability isn't being reduced at all. Even if individual rooms aren't mapped, the total availability for the room type should decrease.</p>
            </div>
          </div>
        </section>

        <!-- Evidence -->
        <section class="section collapsed" id="evidence">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128200;</span>
            <div>
              <h2 class="section-title">
                Evidence
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Key observations and calendar comparison</p>
            </div>
          </div>
          <div class="section-content">
            <h3 style="font-size: 1rem; margin-bottom: 1rem; color: var(--text-secondary);">Room Mapping Status (All 8 Room Types)</h3>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Room Type</th>
                    <th>Mapping</th>
                    <th>Read Only</th>
                    <th>Stop Sell</th>
                    <th>Send Price</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Chambre Double Superieur</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Suite Executive</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Suite De Luxe King Size</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Suite Familiale</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Chambre Triple Deluxe</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Chambre Double Deluxe</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Suite</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                  <tr>
                    <td>Suite Presidentielle</td>
                    <td class="status-check">&#10003; Mapped</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-cross">&#10007; No</td>
                    <td class="status-check">&#10003; Yes</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Calendar Availability Discrepancy</h3>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Expected Rooms</th>
                    <th>Actual (Booking.com)</th>
                    <th>Discrepancy</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Dec 31</td>
                    <td><strong>0</strong> (Both Room 4 & 5 occupied)</td>
                    <td><strong>1</strong></td>
                    <td class="discrepancy">&#128308; +1 extra room shown</td>
                  </tr>
                  <tr>
                    <td>Jan 1</td>
                    <td><strong>0</strong> (Both Room 4 & 5 occupied)</td>
                    <td><strong>2</strong></td>
                    <td class="discrepancy">&#128308; +2 extra rooms shown</td>
                  </tr>
                  <tr>
                    <td>Jan 2</td>
                    <td><strong>1</strong> (Only Room 4 occupied)</td>
                    <td><strong>2</strong></td>
                    <td class="discrepancy">&#128308; +1 extra room shown</td>
                  </tr>
                  <tr>
                    <td>Jan 3</td>
                    <td><strong>2</strong> (Both checkout)</td>
                    <td><strong>2</strong></td>
                    <td class="correct">&#10003; Correct</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="mitigation-box">
              <h5>&#9989; UPDATE 2025-12-29</h5>
              <p>Dates Dec 31 - Jan 2 have been <strong>MANUALLY BLOCKED</strong> via Booking.com Open/Close Rooms wizard. The discrepancy above reflects the state BEFORE mitigation was applied. Double-booking risk for these specific dates is now <strong>mitigated</strong>.</p>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Key Observations</h3>

            <div class="table-container">
              <table>
                <thead>
                  <tr>
                    <th>Observation</th>
                    <th>Interpretation</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Booking.com calendar locked ("XML not editable")</td>
                    <td>Channel manager connection active</td>
                  </tr>
                  <tr>
                    <td>Dec 29-30 show "Net booked = 1"</td>
                    <td>Booking.com reservations sync correctly</td>
                  </tr>
                  <tr>
                    <td>Dec 31 - Jan 2 show "Net booked = 0"</td>
                    <td>Internal reservations NOT syncing</td>
                  </tr>
                  <tr>
                    <td>HotelRunner logs show 100% success</td>
                    <td>Transactions may not include internal reservations</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h3 style="font-size: 1rem; margin: 1.5rem 0 1rem; color: var(--text-secondary);">Screenshot References</h3>
            <ol style="margin: 0.5rem 0 0 1.5rem; color: var(--text-secondary);">
              <li>HotelRunner Reservations page showing Gouram & Benchekroune</li>
              <li>Booking.com Calendar showing incorrect availability for Dec 31 - Jan 2</li>
              <li>Booking.com "XML (not editable)" confirmation</li>
              <li>HotelRunner Logs showing 3,588 successful transactions</li>
            </ol>
          </div>
        </section>

        <!-- Recommended Actions -->
        <section class="section" id="actions">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#9745;</span>
            <div>
              <h2 class="section-title">
                Recommended Actions
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Prioritized action items with progress tracking</p>
            </div>
          </div>
          <div class="section-content">
            <div class="action-list" id="action-list">
              <div class="action-group-title">Immediate (Today) - P0</div>

              <div class="action-item checked" data-id="action-1" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p0">P0</span>
                    Manually block Dec 31 - Jan 2 on Booking.com calendar
                  </div>
                  <div class="action-owner">Owner: Claude</div>
                  <div class="action-result">&#10003; "Chambre Double Superieur 4;5" closed via Open/Close Rooms wizard</div>
                </div>
              </div>

              <div class="action-item checked" data-id="action-2" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p0">P0</span>
                    Verify if "Sync Availability" option exists in HotelRunner channel settings
                  </div>
                  <div class="action-owner">Owner: Claude</div>
                  <div class="action-result">&#10003; Found "Allocation Type" setting - currently set to "No changes"</div>
                </div>
              </div>

              <div class="action-item" data-id="action-3" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p0">P0</span>
                    Contact HotelRunner support with this investigation report
                  </div>
                  <div class="action-owner">Owner: Omar</div>
                  <div class="action-status">&#9203; Pending</div>
                </div>
              </div>

              <div class="action-group-title">Short-term (This Week) - P1</div>

              <div class="action-item" data-id="action-4" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p1">P1</span>
                    Review HotelRunner "Allocation Type" dropdown options
                  </div>
                  <div class="action-owner">Owner: Omar</div>
                  <div class="action-status">&#9203; Pending (Claude couldn't open dropdown)</div>
                </div>
              </div>

              <div class="action-item" data-id="action-5" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p1">P1</span>
                    Test "Import reservations" button to force sync
                  </div>
                  <div class="action-owner">Owner: Omar</div>
                  <div class="action-status">&#9203; Pending</div>
                </div>
              </div>

              <div class="action-item" data-id="action-6" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p1">P1</span>
                    Verify Booking.com extranet for any NON-XML settings
                  </div>
                  <div class="action-owner">Owner: Omar</div>
                  <div class="action-status">&#9203; Pending</div>
                </div>
              </div>

              <div class="action-group-title">Medium-term - P2</div>

              <div class="action-item" data-id="action-7" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p2">P2</span>
                    Consider room-level mapping (individual rooms vs room types)
                  </div>
                  <div class="action-owner">Owner: Omar + HotelRunner</div>
                </div>
              </div>

              <div class="action-item" data-id="action-8" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p2">P2</span>
                    Evaluate alternative channel managers if HotelRunner cannot fix
                  </div>
                  <div class="action-owner">Owner: Omar</div>
                </div>
              </div>

              <div class="action-item" data-id="action-9" onclick="toggleAction(this)">
                <div class="action-checkbox">&#10003;</div>
                <div class="action-content">
                  <div class="action-label">
                    <span class="action-priority priority-p2">P2</span>
                    Document SOP for manual calendar sync as workaround
                  </div>
                  <div class="action-owner">Owner: Claude</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Support Ticket -->
        <section class="section" id="support-ticket">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128231;</span>
            <div>
              <h2 class="section-title">
                Support Ticket Draft
                <span class="badge badge-info">UPDATED</span>
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Ready to send to HotelRunner Support (v1.2 with new observations)</p>
            </div>
          </div>
          <div class="section-content">
            <div class="code-header">
              <span class="code-title">Subject: Internal reservations not syncing availability to Booking.com</span>
              <button class="copy-btn" id="copy-ticket" onclick="copyTicket()">
                <span>&#128203;</span> Copy to Clipboard
              </button>
            </div>
            <div class="code-block" id="ticket-content">Property: Villa Thaifa
HR_ID: [Check credentials file]
Connection: Booking.com (Two-Way XML)

Problem:
Reservations created manually on HotelRunner (source: "Online"/internal) do not
reduce availability on Booking.com calendar. This creates double-booking risk.

Specific Example:
- Guest: Sabah Gouram
- Dates: Dec 31, 2025 - Jan 3, 2026
- Room Type: Double Room Superior (Room 4)
- Confirmation: R599233355
- Created on: HotelRunner (internal)

Expected: Booking.com should show 1 room available for Double Room Superior
(2 total - 1 booked = 1 available)

Actual: Booking.com shows 2 rooms available (no reduction)

Observations:
- Channel connection active (XML not editable on Booking.com)
- Room mapping correct (8 room types, no Read Only)
- Transaction logs show 3,588 successes, 0 failures
- Reservations FROM Booking.com appear correctly
- "Allocation Type" setting in Room type mapping > Advanced settings is set to "No changes"
- Last import from Booking.com: December 08, 2025 (3 weeks ago)
- Connectivity status shows "Rate and Availability: Connection is active"

Questions:
1. What does "Allocation Type: No changes" mean? Should this be changed to enable availability sync?
2. How do we trigger a manual sync to push availability updates to Booking.com?
3. Why hasn't the import run automatically since December 08?
4. Is there a setting to enable availability sync for internal/manual reservations?

Please advise urgently - we risk double-bookings during high season.

Thank you,
Villa Thaifa Management</div>
          </div>
        </section>

        <!-- Update Log -->
        <section class="section" id="update-log">
          <div class="section-header" onclick="toggleSection(this.parentElement)">
            <span class="section-icon">&#128197;</span>
            <div>
              <h2 class="section-title">
                Update Log
                <span class="collapse-icon">&#9660;</span>
              </h2>
              <p class="section-subtitle">Report version history</p>
            </div>
          </div>
          <div class="section-content">
            <div class="table-container update-log">
              <table>
                <thead>
                  <tr>
                    <th>Date</th>
                    <th>Version</th>
                    <th>Changes</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>2025-12-29</td>
                    <td>1.0</td>
                    <td>Initial investigation report</td>
                  </tr>
                  <tr>
                    <td>2025-12-29</td>
                    <td>1.1</td>
                    <td>P0 actions completed: Booking.com dates blocked, HotelRunner settings audited</td>
                  </tr>
                  <tr class="current">
                    <td>2025-12-29</td>
                    <td><strong>1.2</strong></td>
                    <td>Added connectivity evidence, updated support ticket, calendar mitigation note, Allocation Type caveat</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>

      </div>
    </main>

    <footer class="footer">
      <div class="footer-content">
        <span>Investigation completed: 2025-12-29 | P0 Actions completed: 2025-12-29</span>
        <span>Report version: 1.2</span>
      </div>
    </footer>
  </div>

  <script>
    (function() {
      'use strict';

      const THEME_KEY = 'sync-report-theme';
      const ACTIONS_KEY = 'sync-report-actions';

      // Theme Toggle
      function loadTheme() {
        const theme = localStorage.getItem(THEME_KEY) || 'dark';
        document.documentElement.setAttribute('data-theme', theme);
      }

      function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem(THEME_KEY, next);
      }

      // Section Collapse
      window.toggleSection = function(section) {
        section.classList.toggle('collapsed');
      };

      // Action Items
      function loadActions() {
        const stored = localStorage.getItem(ACTIONS_KEY);
        if (stored) {
          const checked = JSON.parse(stored);
          checked.forEach(id => {
            const item = document.querySelector(`.action-item[data-id="${id}"]`);
            if (item) {
              item.classList.add('checked');
            }
          });
        }
      }

      function saveActions() {
        const checked = [];
        document.querySelectorAll('.action-item.checked').forEach(item => {
          checked.push(item.dataset.id);
        });
        localStorage.setItem(ACTIONS_KEY, JSON.stringify(checked));
      }

      window.toggleAction = function(item) {
        item.classList.toggle('checked');
        saveActions();
      };

      // Copy to Clipboard
      window.copyTicket = function() {
        const content = document.getElementById('ticket-content').textContent;
        const btn = document.getElementById('copy-ticket');

        navigator.clipboard.writeText(content).then(() => {
          btn.classList.add('copied');
          btn.innerHTML = '<span>&#10003;</span> Copied!';

          setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<span>&#128203;</span> Copy to Clipboard';
          }, 2000);
        }).catch(err => {
          console.error('Failed to copy:', err);
          // Fallback for older browsers
          const textarea = document.createElement('textarea');
          textarea.value = content;
          document.body.appendChild(textarea);
          textarea.select();
          document.execCommand('copy');
          document.body.removeChild(textarea);

          btn.classList.add('copied');
          btn.innerHTML = '<span>&#10003;</span> Copied!';

          setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<span>&#128203;</span> Copy to Clipboard';
          }, 2000);
        });
      };

      // Smooth scroll for nav links
      document.querySelectorAll('.nav-item').forEach(link => {
        link.addEventListener('click', function(e) {
          e.preventDefault();
          const targetId = this.getAttribute('href').substring(1);
          const target = document.getElementById(targetId);
          if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        });
      });

      // Print functionality
      function printReport() {
        window.print();
      }

      // Initialize
      function init() {
        loadTheme();
        loadActions();

        document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
        document.getElementById('print-btn').addEventListener('click', printReport);
      }

      document.addEventListener('DOMContentLoaded', init);
    })();
  </script>
</body>
</html>
