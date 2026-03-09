#!/usr/bin/env python3
"""Replace CSS with clean, Apple-like minimal design"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New Apple-inspired CSS - clean, minimal, professional
new_css = """        /* ============================================
           TOWNSQUARE - CLEAN & PROFESSIONAL DESIGN
           Apple-inspired minimalism
           ============================================ */

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        /* ── Smooth Color Palette ─────────────────── */
        :root {
            /* Softer Primary Colors */
            --primary: #667eea;
            --primary-light: #818cf8;
            --primary-dark: #4f46e5;
            
            /* Softer Accents */
            --accent: #f43f5e;
            --accent-light: #fb7185;
            --accent-cyan: #06b6d4;
            
            /* Neutrals */
            --neutral-dark: #1e293b;
            --neutral-gray: #64748b;
            --neutral-light: #f1f5f9;
            --neutral-white: #ffffff;
            
            /* Status Colors */
            --success: #10b981;
            --warning: #f59e0b;
            --error: #ef4444;
            
            /* Smooth Shadows */
            --shadow-sm: 0 2px 8px rgba(102, 126, 234, 0.08);
            --shadow-md: 0 8px 24px rgba(102, 126, 234, 0.12);
            --shadow-lg: 0 16px 48px rgba(102, 126, 234, 0.18);
            --shadow-xl: 0 24px 64px rgba(102, 126, 234, 0.24);
            
            /* Light Mode (default) */
            --bg-primary: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
            --bg-secondary: rgba(255, 255, 255, 0.7);
            --bg-glass: rgba(255, 255, 255, 0.8);
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --card-bg: rgba(255, 255, 255, 0.9);
            --border-color: rgba(102, 126, 234, 0.1);
            
            /* Glassmorphism */
            --glass-blur: blur(16px);
        }

        body.dark-mode {
            --bg-primary: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            --bg-secondary: rgba(30, 41, 59, 0.7);
            --bg-glass: rgba(30, 41, 59, 0.8);
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e1;
            --card-bg: rgba(30, 41, 59, 0.9);
            --border-color: rgba(129, 140, 248, 0.2);
        }

        body {
            font-family: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            transition: background 0.6s cubic-bezier(0.4, 0, 0.2, 1), color 0.6s ease;
            letter-spacing: 0.01em;
            line-height: 1.6;
        }

        .hidden {
            display: none !important;
        }

        /* ── Floating Background Elements ─────────── */
        .bg-decoration {
            position: fixed;
            border-radius: 50%;
            opacity: 0.04;
            z-index: 0;
            pointer-events: none;
            filter: blur(80px);
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -30px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }

        .circle-1 {
            width: 500px;
            height: 500px;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            top: -150px;
            right: -150px;
            animation-delay: 0s;
        }

        .circle-2 {
            width: 400px;
            height: 400px;
            background: linear-gradient(135deg, var(--accent-cyan), var(--primary));
            bottom: -100px;
            left: -100px;
            animation-delay: 7s;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        /* ── Main Layout ──────────────────────────── */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            position: relative;
            z-index: 10;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
            animation: fadeIn 1s ease 0s both;
        }

        h1 {
            font-family: 'Fraunces', serif;
            font-size: 4rem;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            letter-spacing: -1px;
            line-height: 1.1;
            font-weight: 700;
            animation: fadeIn 1s ease 0.1s both;
        }

        .tagline {
            font-size: 1.3rem;
            background: linear-gradient(135deg, var(--accent), var(--accent-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 600;
            margin-bottom: 1.2rem;
            letter-spacing: 0.5px;
            animation: fadeIn 1s ease 0.2s both;
        }

        h2 {
            font-family: 'Fraunces', serif;
            font-size: 2.25rem;
            color: var(--text-primary);
            margin-bottom: 1.5rem;
            font-weight: 700;
            animation: fadeIn 0.8s ease 0.15s both;
        }

        h3 {
            font-size: 1.4rem;
            color: var(--text-primary);
            margin-bottom: 0.75rem;
            font-weight: 600;
        }

        p {
            font-size: 1rem;
            color: var(--text-secondary);
            line-height: 1.7;
        }

        /* ── Hero Section - Glassmorphism ─────────── */
        .hero-section {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            border-radius: 32px;
            padding: 4rem 3rem;
            margin-bottom: 3rem;
            box-shadow: var(--shadow-lg);
            text-align: center;
            animation: fadeIn 1s cubic-bezier(0.4, 0, 0.2, 1) 0.2s both;
            position: relative;
            overflow: hidden;
            border: 1px solid var(--border-color);
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;
        }

        .hero-section:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-xl);
        }

        .hero-section::before {
            content: '';
            position: absolute;
            inset: -50%;
            background: linear-gradient(45deg, transparent 30%, rgba(102, 126, 234, 0.03), transparent 70%);
            animation: rotate 8s linear infinite;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* ── Stats Section - Floating Cards ────────── */
        .stats-section {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            border-radius: 32px;
            padding: 4rem 2rem;
            margin-bottom: 3rem;
            box-shadow: var(--shadow-xl);
            animation: fadeIn 1s ease 0.4s both;
            position: relative;
            overflow: hidden;
        }

        .stats-section::before {
            content: '';
            position: absolute;
            inset: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="1" fill="rgba(255,255,255,0.05)"/></svg>');
            background-size: 20px 20px;
            opacity: 0.3;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            position: relative;
            z-index: 1;
        }

        .stat-item {
            text-align: center;
            color: var(--neutral-white);
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
            padding: 1.5rem;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .stat-item:hover {
            transform: translateY(-8px) scale(1.05);
            background: rgba(255, 255, 255, 0.15);
        }

        .stat-item.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .stat-item:nth-child(1).visible { transition-delay: 0.1s; }
        .stat-item:nth-child(2).visible { transition-delay: 0.2s; }
        .stat-item:nth-child(3).visible { transition-delay: 0.3s; }
        .stat-item:nth-child(4).visible { transition-delay: 0.4s; }

        .stat-number {
            font-family: 'Fraunces', serif;
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1;
            margin-bottom: 0.6rem;
            display: block;
            background: linear-gradient(135deg, #fff, rgba(255,255,255,0.8));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .stat-label {
            font-size: 0.95rem;
            opacity: 0.9;
            font-weight: 500;
            letter-spacing: 0.5px;
        }

        /* ── Auth Section - Glass Card ────────────── */
        .auth-container {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            border-radius: 32px;
            padding: 3rem;
            box-shadow: var(--shadow-lg);
            max-width: 500px;
            margin: 0 auto 3rem;
            animation: fadeIn 1s ease 0.3s both;
            border: 1px solid var(--border-color);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        .auth-container:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-xl);
        }

        .auth-toggle {
            display: flex;
            gap: 0.75rem;
            margin-bottom: 2rem;
            background: var(--bg-secondary);
            backdrop-filter: var(--glass-blur);
            padding: 0.5rem;
            border-radius: 20px;
        }

        .auth-tab {
            flex: 1;
            padding: 1rem;
            border: none;
            background: transparent;
            color: var(--text-primary);
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            border-radius: 16px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            font-family: 'Manrope', sans-serif;
        }

        .auth-tab:hover {
            background: rgba(102, 126, 234, 0.1);
        }

        .auth-tab.active {
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: var(--neutral-white);
            transform: scale(1.02);
            box-shadow: var(--shadow-md);
        }

        input, textarea, select {
            width: 100%;
            padding: 1rem 1.25rem;
            border: 2px solid var(--border-color);
            border-radius: 16px;
            font-size: 0.95rem;
            font-family: 'Manrope', sans-serif;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: var(--bg-secondary);
            backdrop-filter: var(--glass-blur);
            color: var(--text-primary);
        }

        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        /* ── Smooth Buttons ──────────────────────── */
        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 16px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            font-family: 'Manrope', sans-serif;
            display: inline-block;
            letter-spacing: 0.3px;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .btn:active::before {
            width: 300px;
            height: 300px;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: var(--neutral-white);
            width: 100%;
            box-shadow: var(--shadow-md);
        }

        .btn-primary:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: var(--shadow-lg);
        }

        .btn-secondary {
            background: var(--bg-secondary);
            backdrop-filter: var(--glass-blur);
            color: var(--text-primary);
            border: 2px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: var(--primary);
            color: white;
            border-color: var(--primary);
            transform: translateY(-2px);
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        /* ── User Bar - Glass Effect ─────────────── */
        .user-bar {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            color: var(--text-primary);
            padding: 1.5rem 2rem;
            border-radius: 24px;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: var(--shadow-md);
            flex-wrap: wrap;
            gap: 1rem;
            border: 1px solid var(--border-color);
            transition: all 0.4s ease;
        }

        .user-bar:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .user-info {
            font-size: 1.1rem;
            font-weight: 600;
        }

        .user-info span {
            background: linear-gradient(135deg, var(--accent), var(--accent-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .dark-mode-toggle {
            background: rgba(102, 126, 234, 0.1);
            backdrop-filter: var(--glass-blur);
            border: none;
            padding: 0.7rem 1.2rem;
            border-radius: 16px;
            color: var(--text-primary);
            cursor: pointer;
            font-family: 'Manrope', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .dark-mode-toggle:hover {
            background: rgba(102, 126, 234, 0.2);
            transform: scale(1.05);
        }

        /* ── Smooth Navigation Taskbar ───────────── */
        .nav-taskbar {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            border-radius: 24px;
            padding: 1rem 1.5rem;
            margin-bottom: 2rem;
            box-shadow: var(--shadow-md);
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            justify-content: flex-start;
            align-items: center;
            position: sticky;
            top: 1rem;
            z-index: 30;
            opacity: 0;
            transform: translateY(-20px);
            transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
            border: 1px solid var(--border-color);
        }

        .nav-taskbar.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .nav-tab-btn {
            background: transparent;
            border: none;
            padding: 0.85rem 1.5rem;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            font-family: 'Manrope', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.6rem;
            position: relative;
            white-space: nowrap;
            flex: 1 1 auto;
            min-width: 120px;
        }

        .nav-tab-btn::before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            transform: translateX(-50%);
            transition: width 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            border-radius: 3px 3px 0 0;
        }

        .nav-tab-btn:hover {
            background: rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }

        .nav-tab-btn.active {
            background: linear-gradient(135deg, var(--primary), var(--primary-light));
            color: var(--neutral-white);
            box-shadow: var(--shadow-sm);
            transform: scale(1.05);
        }

        .nav-tab-btn.active::before {
            width: 70%;
        }

        /* ── Smooth Business Cards ───────────────── */
        .business-card {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            border-radius: 28px;
            overflow: hidden;
            box-shadow: var(--shadow-md);
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            opacity: 0;
            transform: translateY(30px);
            border: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .business-card:hover {
            transform: translateY(-12px) scale(1.02);
            box-shadow: var(--shadow-xl);
        }

        .business-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            padding: 2.5rem 2rem;
            color: var(--neutral-white);
            min-height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            position: relative;
            isolation: isolate;
        }

        .business-header::before {
            content: '';
            position: absolute;
            inset: 0;
            background-size: cover;
            background-position: center;
            opacity: 0.2;
            z-index: -2;
            transition: opacity 0.4s ease;
        }

        .business-card:hover .business-header::before {
            opacity: 0.3;
        }

        .business-name {
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            letter-spacing: -0.5px;
        }

        .business-category {
            display: inline-block;
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .business-body {
            padding: 1.75rem;
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .business-description {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.6;
            flex: 1;
        }

        .rating-stars {
            display: flex;
            gap: 0.3rem;
            margin-bottom: 1rem;
            justify-content: flex-start;
        }

        .star {
            color: var(--warning);
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .star:hover {
            transform: scale(1.3) rotate(10deg);
        }

        .deal-badge {
            background: linear-gradient(135deg, var(--accent-light), var(--accent));
            color: var(--neutral-white);
            padding: 1.2rem 1.5rem;
            border-radius: 16px;
            font-weight: 700;
            text-align: center;
            font-size: 0.95rem;
            letter-spacing: 0.3px;
            box-shadow: var(--shadow-md);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .deal-badge:hover {
            transform: scale(1.05);
            box-shadow: var(--shadow-lg);
        }

        /* ── Content Sections ─────────────────────── */
        .section {
            margin-bottom: 4rem;
            animation: fadeIn 1s ease 0.3s both;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 2rem;
            color: var(--text-primary);
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        /* ── Footer ───────────────────────────────── */
        footer {
            background: var(--card-bg);
            backdrop-filter: var(--glass-blur);
            border-top: 1px solid var(--border-color);
            padding: 3rem 2rem;
            text-align: center;
            color: var(--text-secondary);
            margin-top: 4rem;
            border-radius: 32px 32px 0 0;
        }

        /* ── Media Queries ────────────────────────── */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }

            h2 {
                font-size: 1.75rem;
            }

            .container {
                padding: 1rem;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .hero-section {
                padding: 2rem 1.5rem;
            }

            .nav-taskbar {
                flex-direction: column;
                align-items: stretch;
            }

            .nav-tab-btn {
                flex: 1;
            }

            .user-bar {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 480px) {
            h1 {
                font-size: 2rem;
            }

            h2 {
                font-size: 1.3rem;
            }

            .stat-number {
                font-size: 2.5rem;
            }

            .stats-grid {
                grid-template-columns: 1fr;
            }

            .btn {
                padding: 0.85rem 1.5rem;
                font-size: 0.9rem;
            }

            .auth-container {
                padding: 2rem 1.5rem;
            }

            .hero-section {
                padding: 1.5rem;
            }
        }
"""

# Find and replace the CSS content
style_start = content.find('<style>') + len('<style>')
style_end = content.find('</style>')

if style_start > 7 and style_end > style_start:
    # Replace the old CSS with new CSS
    new_content = content[:style_start] + new_css + content[style_end:]
    
    # Write back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ CSS replacement successful!")
    print(f"Replaced {style_end - style_start} characters of old CSS")
    print(f"With {len(new_css)} characters of new CSS")
else:
    print("❌ Could not find style tags")
