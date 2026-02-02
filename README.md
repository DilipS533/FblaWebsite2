<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TownSquare - Your Local Business Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        :root {
            --sunset-orange: #FF6B35;
            --deep-teal: #004E64;
            --warm-cream: #FFF8F0;
            --soft-coral: #FF9F80;
            --midnight: #1A2332;
            --golden: #F7B32B;
            --shadow: rgba(0, 78, 100, 0.15);
            --success-green: #10B981;
            --danger-red: #EF4444;
            
            /* Light mode (default) */
            --bg-primary: #f8f9fa;
            --bg-secondary: #e9ecef;
            --text-primary: #1A2332;
            --text-secondary: #666;
            --card-bg: white;
        }

        body.dark-mode {
            --bg-primary: #1a1a2e;
            --bg-secondary: #16213e;
            --text-primary: #eee;
            --text-secondary: #aaa;
            --card-bg: #0f3460;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            transition: background 0.3s ease, color 0.3s ease;
        }

        /* Animated background elements */
        .bg-decoration {
            position: fixed;
            border-radius: 50%;
            opacity: 0.1;
            z-index: 0;
            pointer-events: none;
            will-change: transform;
        }

        .circle-1 {
            width: 400px;
            height: 400px;
            background: var(--sunset-orange);
            top: -100px;
            right: -100px;
            animation: float 20s infinite ease-in-out;
        }

        .circle-2 {
            width: 300px;
            height: 300px;
            background: var(--deep-teal);
            bottom: -50px;
            left: -50px;
            animation: float 25s infinite ease-in-out reverse;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg) scale(1); }
            33% { transform: translate(30px, -30px) rotate(120deg) scale(1.1); }
            66% { transform: translate(-20px, 20px) rotate(240deg) scale(0.9); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
            position: relative;
            z-index: 1;
        }

        /* FBLA Disclaimer Overlay */
        .disclaimer-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.85);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease-out;
        }

        .disclaimer-overlay.hidden {
            display: none;
        }

        .disclaimer-content {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            max-width: 600px;
            width: 90%;
            text-align: center;
            animation: slideUp 0.5s ease-out;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .fbla-logo {
            font-size: 4rem;
            margin-bottom: 1rem;
        }

        .disclaimer-title {
            font-family: 'DM Serif Display', serif;
            font-size: 2.5rem;
            color: #003DA5;
            margin-bottom: 1rem;
        }

        .disclaimer-text {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #333;
            margin-bottom: 2rem;
        }

        .disclaimer-highlight {
            background: #FEF3C7;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            border-left: 4px solid #F59E0B;
        }

        .disclaimer-highlight strong {
            color: #B45309;
        }

        /* FBLA Banner */
        .fbla-banner {
            background: linear-gradient(135deg, #003DA5 0%, #0052CC 100%);
            color: white;
            padding: 1rem 2rem;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 61, 165, 0.3);
            position: relative;
            overflow: hidden;
        }

        .fbla-banner::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 50%, transparent 70%);
            animation: shimmer 3s infinite;
        }

        @keyframes shimmer {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }

        .fbla-content {
            position: relative;
            z-index: 1;
        }

        .fbla-title {
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: 1px;
        }

        /* Header */
        header {
            text-align: center;
            margin-bottom: 3rem;
            animation: slideDown 0.8s ease-out;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-section {
            background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
            border-radius: 25px;
            padding: 4rem 3rem;
            margin-bottom: 3rem;
            box-shadow: 0 20px 60px var(--shadow);
            text-align: center;
            animation: fadeIn 1s ease-out 0.2s both;
            position: relative;
            overflow: hidden;
        }

        /* Town Hall Building Illustration */
        .hero-section::before {
            content: '';
            position: absolute;
            bottom: -20px;
            left: 50%;
            transform: translateX(-50%);
            width: 300px;
            height: 250px;
            background: linear-gradient(to bottom, #004E64 0%, #003d50 100%);
            opacity: 0.05;
            clip-path: polygon(
                20% 100%, 20% 40%, 30% 40%, 30% 35%, 25% 30%, 25% 25%, 30% 25%, 30% 20%, 70% 20%, 70% 25%, 75% 25%, 75% 30%, 70% 35%, 70% 40%, 80% 40%, 80% 100%,
                45% 100%, 45% 70%, 55% 70%, 55% 100%
            );
        }

        /* Clock tower/dome on top */
        .hero-section::after {
            content: '';
            position: absolute;
            bottom: 210px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 80px;
            background: linear-gradient(to bottom, #FF6B35 0%, #ff8555 100%);
            opacity: 0.1;
            clip-path: polygon(0% 60%, 0% 100%, 100% 100%, 100% 60%, 80% 40%, 80% 0%, 50% 20%, 20% 0%, 20% 40%);
        }

        .hero-content {
            position: relative;
            z-index: 1;
        }

        h1 {
            font-family: 'DM Serif Display', serif;
            font-size: 4.5rem;
            color: var(--deep-teal);
            margin-bottom: 1rem;
            letter-spacing: -2px;
            line-height: 1.1;
        }

        .tagline {
            font-size: 1.5rem;
            color: var(--sunset-orange);
            font-weight: 300;
            font-style: italic;
            margin-bottom: 0.5rem;
        }

        .hero-subtitle {
            font-size: 1.2rem;
            color: #666;
            max-width: 700px;
            margin: 1.5rem auto 0;
            line-height: 1.6;
        }

        /* Statistics Section */
        .stats-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 25px;
            padding: 3rem 2rem;
            margin-bottom: 3rem;
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
            animation: fadeIn 1s ease-out 0.4s both;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            max-width: 1000px;
            margin: 0 auto;
        }

        .stat-item {
            text-align: center;
            color: white;
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease-out;
        }

        .stat-item.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .stat-item:nth-child(1).visible { transition-delay: 0.2s; }
        .stat-item:nth-child(2).visible { transition-delay: 0.4s; }
        .stat-item:nth-child(3).visible { transition-delay: 0.6s; }
        .stat-item:nth-child(4).visible { transition-delay: 0.8s; }

        .stat-number {
            font-family: 'DM Serif Display', serif;
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1;
            margin-bottom: 0.5rem;
            display: block;
            background: linear-gradient(to bottom, #ffffff 0%, #f0f0f0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .stat-label {
            font-size: 1.1rem;
            opacity: 0.95;
            font-weight: 400;
        }

        .stat-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            display: block;
        }

        /* Auth Section */
        .auth-container {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 20px 60px var(--shadow);
            max-width: 500px;
            margin: 0 auto 3rem;
            animation: fadeIn 1s ease-out 0.3s both;
        }

        .auth-toggle {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .auth-tab {
            flex: 1;
            padding: 0.75rem;
            border: none;
            background: transparent;
            color: var(--midnight);
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            border-radius: 10px;
            transition: all 0.3s ease;
            font-family: 'Outfit', sans-serif;
        }

        .auth-tab.active {
            background: var(--sunset-orange);
            color: white;
            transform: scale(1.05);
        }

        .input-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: var(--deep-teal);
        }

        input {
            width: 100%;
            padding: 0.875rem 1rem;
            border: 2px solid #E8E8E8;
            border-radius: 10px;
            font-size: 1rem;
            font-family: 'Outfit', sans-serif;
            transition: all 0.3s ease;
        }

        input:focus {
            outline: none;
            border-color: var(--sunset-orange);
            box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
        }

        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 12px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Outfit', sans-serif;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--sunset-orange) 0%, var(--soft-coral) 100%);
            color: white;
            width: 100%;
            box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(255, 107, 53, 0.4);
        }

        .btn-secondary {
            background: white;
            color: var(--deep-teal);
            border: 2px solid var(--deep-teal);
        }

        .btn-secondary:hover {
            background: var(--deep-teal);
            color: white;
        }

        /* Main App */
        .app-container {
            display: none;
            animation: fadeIn 0.8s ease-out;
        }

        .app-container.active {
            display: block;
        }

        .user-bar {
            background: var(--deep-teal);
            color: white;
            padding: 1.5rem 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 10px 40px var(--shadow);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .user-controls {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .dark-mode-toggle {
            background: rgba(255, 255, 255, 0.2);
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            color: white;
            cursor: pointer;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .dark-mode-toggle:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }

        /* Profile Section */
        .profile-section {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px var(--shadow);
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
        }

        .profile-stat {
            text-align: center;
            padding: 1rem;
            border-radius: 10px;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(255, 159, 128, 0.1) 100%);
        }

        .profile-stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: var(--sunset-orange);
            display: block;
            margin-bottom: 0.5rem;
        }

        .profile-stat-label {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        /* Category Pills */
        .category-filter {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: var(--card-bg);
            border-radius: 15px;
        }

        .category-pill {
            padding: 0.5rem 1.25rem;
            border-radius: 20px;
            background: rgba(255, 107, 53, 0.1);
            border: 2px solid transparent;
            color: var(--text-primary);
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .category-pill:hover {
            background: rgba(255, 107, 53, 0.2);
            transform: translateY(-2px);
        }

        .category-pill.active {
            background: var(--sunset-orange);
            color: white;
            border-color: var(--sunset-orange);
        }

        /* Recent Activity */
        .activity-feed {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px var(--shadow);
            max-height: 400px;
            overflow-y: auto;
        }

        .activity-item {
            padding: 1rem;
            border-left: 3px solid var(--sunset-orange);
            margin-bottom: 1rem;
            background: rgba(255, 107, 53, 0.05);
            border-radius: 8px;
        }

        .activity-time {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }

        /* Achievement Badges */
        .badges-section {
            background: var(--card-bg);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 10px 30px var(--shadow);
        }

        .badges-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .badge {
            text-align: center;
            padding: 1rem;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transition: all 0.3s ease;
        }

        .badge:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .badge.locked {
            background: #ddd;
            color: #999;
            opacity: 0.5;
        }

        .badge-icon {
            font-size: 2rem;
            display: block;
            margin-bottom: 0.5rem;
        }

        .badge-name {
            font-size: 0.85rem;
            font-weight: 600;
        }

        .user-info {
            font-size: 1.2rem;
            font-weight: 600;
        }

        .user-info span {
            color: var(--golden);
        }

        /* Navigation Taskbar */
        .nav-taskbar {
            background: white;
            border-radius: 15px;
            padding: 1rem 2rem;
            margin-bottom: 3rem;
            box-shadow: 0 5px 20px var(--shadow);
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transform: translateY(-20px);
            transition: all 0.5s ease-out;
        }

        .nav-taskbar.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .nav-tab-btn {
            background: transparent;
            border: none;
            padding: 1rem 2rem;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: var(--midnight);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            position: relative;
        }

        .nav-tab-btn:hover {
            background: rgba(255, 107, 53, 0.1);
            color: var(--sunset-orange);
            transform: translateY(-2px);
        }

        .nav-tab-btn.active {
            background: linear-gradient(135deg, var(--sunset-orange) 0%, var(--soft-coral) 100%);
            color: white;
            box-shadow: 0 5px 15px rgba(255, 107, 53, 0.3);
        }

        .nav-tab-btn.active::after {
            content: '';
            position: absolute;
            bottom: -1rem;
            left: 50%;
            transform: translateX(-50%);
            width: 0;
            height: 0;
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-top: 8px solid var(--soft-coral);
        }

        .nav-icon-small {
            font-size: 1.2rem;
        }

        /* Remove old nav-grid styles */
        .nav-grid {
            display: none;
        }

        /* Content Sections */
        .content-section {
            display: none;
            animation: fadeIn 0.5s ease-out;
        }

        .content-section.active {
            display: block;
        }

        .section-title {
            font-family: 'DM Serif Display', serif;
            font-size: 2.5rem;
            color: var(--deep-teal);
        }

        /* Filter Controls */
        .filter-controls {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            box-shadow: 0 5px 20px var(--shadow);
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            align-items: center;
            opacity: 0;
            transform: translateX(-30px);
            transition: all 0.6s ease-out;
        }

        .filter-controls.visible {
            opacity: 1;
            transform: translateX(0);
        }

        .search-bar {
            position: relative;
            margin-bottom: 2rem;
            opacity: 0;
            transform: translateX(30px);
            transition: all 0.6s ease-out;
        }

        .search-bar.visible {
            opacity: 1;
            transform: translateX(0);
        }

        .search-input {
            width: 100%;
            padding: 1.25rem 1.5rem;
            padding-left: 3.5rem;
            font-size: 1.1rem;
            border: 2px solid #E8E8E8;
            border-radius: 15px;
            background: white;
        }

        .search-icon {
            position: absolute;
            left: 1.5rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.3rem;
            color: var(--sunset-orange);
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            gap: 1rem;
            opacity: 0;
            transform: translateY(-20px);
            transition: all 0.5s ease-out;
        }

        .section-header.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .filter-label {
            font-weight: 600;
            color: var(--deep-teal);
        }

        .filter-btn {
            padding: 0.75rem 1.5rem;
            border: 2px solid #E8E8E8;
            background: white;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
        }

        .filter-btn.active {
            background: var(--sunset-orange);
            color: white;
            border-color: var(--sunset-orange);
        }

        .filter-btn:hover {
            border-color: var(--sunset-orange);
        }

        /* Business Cards */
        .business-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .business-card {
            background: var(--card-bg);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 30px var(--shadow);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(30px);
        }

        .business-card.visible {
            animation: slideInUp 0.6s ease-out forwards;
        }

        @keyframes slideInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .business-card:nth-child(1).visible { animation-delay: 0.1s; }
        .business-card:nth-child(2).visible { animation-delay: 0.15s; }
        .business-card:nth-child(3).visible { animation-delay: 0.2s; }
        .business-card:nth-child(4).visible { animation-delay: 0.25s; }
        .business-card:nth-child(5).visible { animation-delay: 0.3s; }
        .business-card:nth-child(6).visible { animation-delay: 0.35s; }
        .business-card:nth-child(7).visible { animation-delay: 0.4s; }
        .business-card:nth-child(8).visible { animation-delay: 0.45s; }
        .business-card:nth-child(9).visible { animation-delay: 0.5s; }
        .business-card:nth-child(10).visible { animation-delay: 0.55s; }

        .business-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 20px 60px var(--shadow);
        }

        .business-header {
            background: linear-gradient(135deg, var(--deep-teal) 0%, #006D85 100%);
            padding: 1.5rem;
            color: white;
        }

        .business-name {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .business-category {
            display: inline-block;
            background: rgba(255, 255, 255, 0.2);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }

        .business-body {
            padding: 1.5rem;
        }

        .business-info {
            margin-bottom: 1rem;
        }

        .info-row {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
            color: var(--midnight);
        }

        .rating {
            font-size: 1.5rem;
            color: var(--golden);
            margin-bottom: 0.5rem;
        }

        .review-stats {
            display: flex;
            gap: 1rem;
            margin-top: 0.5rem;
            font-size: 0.9rem;
        }

        .stat-positive {
            color: var(--success-green);
        }

        .stat-negative {
            color: var(--danger-red);
        }

        .deal-badge {
            background: linear-gradient(135deg, var(--sunset-orange) 0%, var(--soft-coral) 100%);
            color: white;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            font-weight: 600;
            margin: 1rem 0;
            text-align: center;
        }

        .business-actions {
            display: flex;
            gap: 0.75rem;
            margin-top: 1rem;
        }

        .btn-small {
            flex: 1;
            padding: 0.75rem;
            font-size: 0.9rem;
        }

        /* Review Section */
        .review-item {
            background: #F8F8F8;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 0.75rem;
            border-left: 4px solid var(--sunset-orange);
        }

        .review-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            align-items: center;
        }

        .review-user {
            font-weight: 600;
            color: var(--deep-teal);
        }

        .review-date {
            font-size: 0.85rem;
            color: #666;
        }

        .review-actions {
            display: flex;
            gap: 1rem;
            margin-top: 0.75rem;
            align-items: center;
        }

        .review-action-btn {
            display: flex;
            align-items: center;
            gap: 0.25rem;
            background: transparent;
            border: none;
            cursor: pointer;
            color: #666;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            padding: 0.25rem 0.5rem;
            border-radius: 5px;
        }

        .review-action-btn:hover {
            background: #E8E8E8;
        }

        .review-action-btn.liked {
            color: var(--success-green);
            font-weight: 600;
        }

        .review-action-btn.disliked {
            color: var(--danger-red);
            font-weight: 600;
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.3s ease-out;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 2.5rem;
            border-radius: 20px;
            max-width: 600px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
            animation: slideUp 0.4s ease-out;
        }

        .modal-header {
            font-family: 'DM Serif Display', serif;
            font-size: 2rem;
            color: var(--deep-teal);
            margin-bottom: 1.5rem;
        }

        .close-modal {
            float: right;
            font-size: 2rem;
            cursor: pointer;
            color: var(--midnight);
            line-height: 1;
            margin-top: -0.5rem;
        }

        .close-modal:hover {
            color: var(--sunset-orange);
        }

        textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #E8E8E8;
            border-radius: 10px;
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            resize: vertical;
            min-height: 100px;
        }

        textarea:focus {
            outline: none;
            border-color: var(--sunset-orange);
            box-shadow: 0 0 0 3px rgba(255, 107, 53, 0.1);
        }

        .star-rating {
            display: flex;
            gap: 0.5rem;
            font-size: 2rem;
            margin: 1rem 0;
            cursor: pointer;
        }

        .star {
            color: #DDD;
            transition: all 0.2s ease;
        }

        .star:hover,
        .star.active {
            color: var(--golden);
            transform: scale(1.2);
        }

        /* CAPTCHA */
        .captcha-container {
            background: #F8F8F8;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            border: 2px solid #E8E8E8;
        }

        .captcha-checkbox {
            display: flex;
            align-items: center;
            gap: 1rem;
            cursor: pointer;
            user-select: none;
        }

        .checkbox {
            width: 30px;
            height: 30px;
            border: 2px solid #999;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: white;
            transition: all 0.3s ease;
        }

        .checkbox.checked {
            background: var(--success-green);
            border-color: var(--success-green);
        }

        .checkmark {
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
        }

        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            color: #666;
        }

        .empty-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            opacity: 0.3;
        }

        /* Responsive */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }

            .tagline {
                font-size: 1rem;
            }

            .hero-section {
                padding: 2rem 1.5rem;
            }

            .business-grid {
                grid-template-columns: 1fr;
            }

            .nav-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .filter-controls {
                flex-direction: column;
                align-items: stretch;
            }
        }

        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>
    <!-- FBLA Disclaimer Overlay -->
    <div id="disclaimerOverlay" class="disclaimer-overlay">
        <div class="disclaimer-content">
            <div class="fbla-logo">🏆</div>
            <h2 class="disclaimer-title">FBLA Educational Project</h2>
            <p class="disclaimer-text">
                This website is created exclusively for Future Business Leaders of America (FBLA) educational purposes.
            </p>
            <div class="disclaimer-highlight">
                <strong>⚠️ IMPORTANT NOTICE:</strong><br>
                All businesses, reviews, user accounts, ratings, and personal information displayed on this website are entirely <strong>fictional and for demonstration purposes only</strong>. No real businesses or individuals are represented.
            </div>
            <p class="disclaimer-text">
                By clicking "I Understand," you acknowledge that this is a student project and all content is simulated.
            </p>
            <button class="btn btn-primary" onclick="acceptDisclaimer()">✓ I Understand</button>
        </div>
    </div>

    <!-- FBLA Educational Purpose Banner -->
    <div class="fbla-banner">
        <div class="fbla-content">
            <div class="fbla-title">🏆 FBLA Project - All Content is Fictional & For Educational Purposes Only</div>
        </div>
    </div>

    <div class="bg-decoration circle-1"></div>
    <div class="bg-decoration circle-2"></div>

    <div class="container">
        <!-- Hero Section -->
        <div class="hero-section">
            <div class="hero-content">
                <h1>TownSquare</h1>
                <p class="tagline">Your guide to our beautiful town</p>
                <p class="hero-subtitle">Discover local gems, read authentic reviews, and support the businesses that make our community thrive. Welcome home.</p>
            </div>
        </div>

        <!-- Auth Section -->
        <div id="authSection" class="auth-container">
            <div class="auth-toggle">
                <button class="auth-tab active" onclick="switchAuthTab('login')">Login</button>
                <button class="auth-tab" onclick="switchAuthTab('register')">Register</button>
            </div>

            <div id="loginForm">
                <div class="input-group">
                    <label>Username</label>
                    <input type="text" id="loginUsername" placeholder="Enter your username">
                </div>
                <div class="input-group">
                    <label>Password</label>
                    <input type="password" id="loginPassword" placeholder="Enter your password">
                </div>
                <button class="btn btn-primary" onclick="login()">Login</button>
                <p style="margin-top: 1rem; text-align: center; color: #666; font-size: 0.9rem;">Demo account: username: <strong>demo</strong>, password: <strong>demo123</strong></p>
            </div>

            <div id="registerForm" class="hidden">
                <div class="input-group">
                    <label>Username</label>
                    <input type="text" id="regUsername" placeholder="Choose a username">
                </div>
                <div class="input-group">
                    <label>Password</label>
                    <input type="password" id="regPassword" placeholder="Choose a password (min 4 characters)">
                </div>
                <button class="btn btn-primary" onclick="register()">Create Account</button>
            </div>
        </div>

        <!-- Main App -->
        <div id="appContainer" class="app-container">
            <div class="user-bar">
                <div class="user-info">Welcome, <span id="currentUser">User</span>!</div>
                <div class="user-controls">
                    <button class="dark-mode-toggle" onclick="toggleDarkMode()">
                        <span id="darkModeIcon">🌙</span>
                        <span id="darkModeText">Dark Mode</span>
                    </button>
                    <button class="btn btn-secondary" onclick="toggleProfile()">👤 Profile</button>
                    <button class="btn btn-secondary" onclick="showHelp()">❓ Help</button>
                    <button class="btn btn-secondary" onclick="logout()">Logout</button>
                </div>
            </div>

            <!-- Profile Section -->
            <div id="profileSection" class="profile-section hidden">
                <div class="profile-stat">
                    <span class="profile-stat-number" id="userReviewCount">0</span>
                    <span class="profile-stat-label">Reviews Written</span>
                </div>
                <div class="profile-stat">
                    <span class="profile-stat-number" id="userFavoriteCount">0</span>
                    <span class="profile-stat-label">Favorites</span>
                </div>
                <div class="profile-stat">
                    <span class="profile-stat-number" id="userLikesGiven">0</span>
                    <span class="profile-stat-label">Likes Given</span>
                </div>
                <div class="profile-stat">
                    <span class="profile-stat-number" id="userBadgeCount">0</span>
                    <span class="profile-stat-label">Badges Earned</span>
                </div>
            </div>

            <!-- Achievement Badges -->
            <div id="badgesSection" class="badges-section hidden">
                <h3 style="margin-bottom: 1rem; color: var(--text-primary);">🏆 Your Achievements</h3>
                <div class="badges-grid">
                    <div class="badge" id="badge-first-review">
                        <span class="badge-icon">✍️</span>
                        <span class="badge-name">First Review</span>
                    </div>
                    <div class="badge locked" id="badge-reviewer">
                        <span class="badge-icon">⭐</span>
                        <span class="badge-name">5 Reviews</span>
                    </div>
                    <div class="badge locked" id="badge-explorer">
                        <span class="badge-icon">🗺️</span>
                        <span class="badge-name">Explorer</span>
                    </div>
                    <div class="badge locked" id="badge-supporter">
                        <span class="badge-icon">💙</span>
                        <span class="badge-name">Supporter</span>
                    </div>
                </div>
            </div>

            <!-- Recent Activity Feed -->
            <div id="activitySection" class="activity-feed hidden">
                <h3 style="margin-bottom: 1rem; color: var(--text-primary);">📋 Recent Activity</h3>
                <div id="activityList"></div>
            </div>

            <!-- Statistics Section -->
            <div class="stats-section">
                <div class="stats-grid">
                    <div class="stat-item">
                        <span class="stat-icon">🏪</span>
                        <span class="stat-number" id="statBusinesses">10</span>
                        <span class="stat-label">Local Businesses</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-icon">⭐</span>
                        <span class="stat-number" id="statReviews">40+</span>
                        <span class="stat-label">Community Reviews</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-icon">👥</span>
                        <span class="stat-number" id="statUsers">100+</span>
                        <span class="stat-label">Active Members</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-icon">💰</span>
                        <span class="stat-number" id="statDeals">10</span>
                        <span class="stat-label">Exclusive Deals</span>
                    </div>
                </div>
            </div>

            <!-- Navigation Taskbar -->
            <div id="navigationTaskbar" class="nav-taskbar">
                <button class="nav-tab-btn active" data-section="browse" onclick="switchTab('browse')">
                    <span class="nav-icon-small">🏪</span>
                    <span>Browse Businesses</span>
                </button>
                <button class="nav-tab-btn" data-section="favorites" onclick="switchTab('favorites')">
                    <span class="nav-icon-small">💙</span>
                    <span>My Favorites</span>
                </button>
                <button class="nav-tab-btn" data-section="deals" onclick="switchTab('deals')">
                    <span class="nav-icon-small">💰</span>
                    <span>Hot Deals</span>
                </button>
                <button class="nav-tab-btn" data-section="recommendations" onclick="switchTab('recommendations')">
                    <span class="nav-icon-small">🎯</span>
                    <span>Recommended</span>
                </button>
            </div>

            <!-- Browse Section -->
            <div id="browseSection" class="content-section">
                <div class="section-header">
                    <h2 class="section-title">All Businesses</h2>
                    <button class="btn btn-secondary" onclick="sortByRating()">Sort by Rating</button>
                </div>

                <div class="category-filter">
                    <span style="font-weight: 600; color: var(--text-primary);">Categories:</span>
                    <button class="category-pill active" onclick="filterByCategory('all')">All</button>
                    <button class="category-pill" onclick="filterByCategory('Food & Dining')">🍽️ Food & Dining</button>
                    <button class="category-pill" onclick="filterByCategory('Services')">🔧 Services</button>
                    <button class="category-pill" onclick="filterByCategory('Health & Wellness')">💪 Health & Wellness</button>
                    <button class="category-pill" onclick="filterByCategory('Retail')">🛍️ Retail</button>
                </div>

                <div class="filter-controls">
                    <span class="filter-label">Filter by:</span>
                    <button class="filter-btn active" onclick="filterReviews('all')">All Businesses</button>
                    <button class="filter-btn" onclick="filterReviews('positive')">Mostly Positive</button>
                    <button class="filter-btn" onclick="filterReviews('negative')">Has Negative Reviews</button>
                    <button class="filter-btn" onclick="filterReviews('highly-rated')">4+ Stars</button>
                </div>

                <div class="search-bar">
                    <span class="search-icon">🔍</span>
                    <input type="text" class="search-input" id="searchInput" placeholder="Search by name or category..." oninput="searchBusinesses()">
                </div>
                <div id="businessGrid" class="business-grid"></div>
            </div>

            <!-- Favorites Section -->
            <div id="favoritesSection" class="content-section">
                <div class="section-header">
                    <h2 class="section-title">My Favorites</h2>
                </div>
                <div id="favoritesGrid" class="business-grid"></div>
            </div>

            <!-- Deals Section -->
            <div id="dealsSection" class="content-section">
                <div class="section-header">
                    <h2 class="section-title">Current Deals</h2>
                </div>
                <div id="dealsGrid" class="business-grid"></div>
            </div>

            <!-- Recommendations Section -->
            <div id="recommendationsSection" class="content-section">
                <div class="section-header">
                    <h2 class="section-title">Recommended for You</h2>
                </div>
                <div id="recommendationsGrid" class="business-grid"></div>
            </div>
        </div>
    </div>

    <!-- Review Modal -->
    <div id="reviewModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeReviewModal()">×</span>
            <h3 class="modal-header">Write a Review</h3>
            <p style="margin-bottom: 1rem; color: #666;">Reviewing: <strong id="reviewBusinessName"></strong></p>
            
            <label>Your Rating</label>
            <div class="star-rating" id="starRating">
                <span class="star" data-rating="1" onclick="setRating(1)">★</span>
                <span class="star" data-rating="2" onclick="setRating(2)">★</span>
                <span class="star" data-rating="3" onclick="setRating(3)">★</span>
                <span class="star" data-rating="4" onclick="setRating(4)">★</span>
                <span class="star" data-rating="5" onclick="setRating(5)">★</span>
            </div>

            <div class="input-group">
                <label>Your Review</label>
                <textarea id="reviewText" placeholder="Share your experience..."></textarea>
            </div>

            <div class="captcha-container">
                <div class="captcha-checkbox" onclick="toggleCaptcha()">
                    <div class="checkbox" id="captchaCheckbox">
                        <span class="checkmark hidden" id="captchaCheck">✓</span>
                    </div>
                    <span style="font-weight: 600;">I'm not a robot</span>
                </div>
            </div>

            <button class="btn btn-primary" onclick="submitReview()">Submit Review</button>
        </div>
    </div>

    <!-- Help Modal -->
    <div id="helpModal" class="modal">
        <div class="modal-content">
            <span class="close-modal" onclick="closeHelpModal()">×</span>
            <h3 class="modal-header">📖 TownSquare Help Guide</h3>
            
            <div style="max-height: 400px; overflow-y: auto;">
                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">🏪 Browse Businesses</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>Click "Browse Businesses" to see all local businesses</li>
                    <li>Use category filters to narrow by type</li>
                    <li>Use review filters to find highly-rated businesses</li>
                    <li>Search by name or category</li>
                </ul>

                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">⭐ Reviews & Ratings</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>Click "Review" on any business card</li>
                    <li>Rate 1-5 stars and write your experience</li>
                    <li>Complete the "I'm not a robot" verification</li>
                    <li>Like/dislike other reviews to help the community</li>
                </ul>

                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">💙 Favorites</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>Click the heart button to save favorites</li>
                    <li>View all favorites in "My Favorites" tab</li>
                    <li>Get personalized recommendations based on your favorites</li>
                </ul>

                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">💰 Hot Deals</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>View current deals and special offers</li>
                    <li>All businesses display their latest promotions</li>
                </ul>

                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">👤 Profile</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>Track your statistics and achievements</li>
                    <li>View recent activity</li>
                    <li>Earn badges for participation</li>
                </ul>

                <h4 style="color: var(--sunset-orange); margin-top: 1rem;">🌙 Dark Mode</h4>
                <ul style="line-height: 1.8; color: var(--text-primary);">
                    <li>Toggle between light and dark themes</li>
                    <li>Preference is saved automatically</li>
                </ul>
            </div>

            <p style="margin-top: 2rem; text-align: center; color: var(--text-secondary);">
                Need more help? Contact support@townsquare.com
            </p>
        </div>
    </div>

    <script>
        // ============================================
        // DATA INITIALIZATION
        // ============================================
        
        /**
         * Business data structure - stores all local businesses
         * Each business has: id, name, category, address, phone, deal, reviews[]
         */
        let businesses = [
            {
                id: 1,
                name: "The Morning Brew Café",
                category: "Food & Dining",
                address: "123 Main Street",
                phone: "(555) 123-4567",
                deal: "Buy 2 coffees, get 1 free",
                reviews: [
                    {user: "sarah_j", rating: 5, text: "Best coffee in town! The baristas are so friendly and the atmosphere is perfect for working.", date: "2025-01-20", likes: 12, dislikes: 1},
                    {user: "mike_smith", rating: 4, text: "Great selection of pastries. Coffee is good but a bit pricey.", date: "2025-01-18", likes: 8, dislikes: 2},
                    {user: "emily_rose", rating: 5, text: "Love this place! Their vanilla latte is incredible.", date: "2025-01-15", likes: 15, dislikes: 0},
                    {user: "john_doe", rating: 3, text: "Good coffee but can get crowded during morning rush.", date: "2025-01-12", likes: 5, dislikes: 3}
                ]
            },
            {
                id: 2,
                name: "TechRepair Pro",
                category: "Services",
                address: "456 Oak Avenue",
                phone: "(555) 234-5678",
                deal: "Free diagnostic for first-time customers",
                reviews: [
                    {user: "alex_tech", rating: 5, text: "Fixed my laptop in under 2 hours! Incredible service and fair prices.", date: "2025-01-19", likes: 20, dislikes: 0},
                    {user: "lisa_m", rating: 5, text: "Highly recommend! They saved all my data when my phone died.", date: "2025-01-16", likes: 18, dislikes: 1},
                    {user: "david_k", rating: 4, text: "Good work, just took a bit longer than expected.", date: "2025-01-14", likes: 6, dislikes: 2}
                ]
            },
            {
                id: 3,
                name: "Green Valley Grocery",
                category: "Food & Dining",
                address: "789 Pine Road",
                phone: "(555) 345-6789",
                deal: "20% off organic produce every Wednesday",
                reviews: [
                    {user: "healthy_living", rating: 5, text: "Amazing selection of organic products! Fresh produce every day.", date: "2025-01-21", likes: 14, dislikes: 0},
                    {user: "budget_shopper", rating: 2, text: "Quality is good but prices are way too high for regular shopping.", date: "2025-01-17", likes: 9, dislikes: 12},
                    {user: "vegan_foodie", rating: 5, text: "Best place for plant-based options! Staff is super helpful.", date: "2025-01-13", likes: 11, dislikes: 1},
                    {user: "tom_reviews", rating: 4, text: "Great variety, wish they had longer opening hours.", date: "2025-01-10", likes: 7, dislikes: 2}
                ]
            },
            {
                id: 4,
                name: "Zen Yoga Studio",
                category: "Health & Wellness",
                address: "321 Wellness Way",
                phone: "(555) 456-7890",
                deal: "First class free for new members",
                reviews: [
                    {user: "yoga_lover", rating: 5, text: "Transformative experience! The instructors are world-class.", date: "2025-01-22", likes: 16, dislikes: 0},
                    {user: "fitness_fan", rating: 4, text: "Great studio, but parking can be difficult during peak hours.", date: "2025-01-19", likes: 8, dislikes: 3},
                    {user: "mindful_me", rating: 5, text: "Beautiful space, calming atmosphere. Highly recommend the evening classes.", date: "2025-01-11", likes: 13, dislikes: 1}
                ]
            },
            {
                id: 5,
                name: "Bella's Italian Kitchen",
                category: "Food & Dining",
                address: "555 Pasta Lane",
                phone: "(555) 567-8901",
                deal: "Free appetizer with any entree after 5pm",
                reviews: [
                    {user: "food_critic_99", rating: 5, text: "Authentic Italian cuisine! The lasagna is to die for.", date: "2025-01-23", likes: 22, dislikes: 1},
                    {user: "pizza_fan", rating: 4, text: "Great pizza and pasta. Service could be faster during busy times.", date: "2025-01-20", likes: 10, dislikes: 4},
                    {user: "maria_g", rating: 5, text: "Reminds me of my grandmother's cooking. Absolutely delicious!", date: "2025-01-18", likes: 19, dislikes: 0},
                    {user: "casual_diner", rating: 3, text: "Food is good but portions are a bit small for the price.", date: "2025-01-15", likes: 6, dislikes: 8},
                    {user: "italian_expert", rating: 5, text: "Best tiramisu I've ever had outside of Italy!", date: "2025-01-12", likes: 17, dislikes: 2}
                ]
            },
            {
                id: 6,
                name: "Bookworm Haven",
                category: "Retail",
                address: "888 Library Street",
                phone: "(555) 678-9012",
                deal: "Buy 2 books, get 1 50% off",
                reviews: [
                    {user: "avid_reader", rating: 5, text: "Cozy bookstore with excellent selection! Love the reading nook.", date: "2025-01-21", likes: 15, dislikes: 0},
                    {user: "book_collector", rating: 4, text: "Good variety but could use more rare/vintage books.", date: "2025-01-17", likes: 7, dislikes: 2},
                    {user: "student_life", rating: 5, text: "Perfect study spot. Great coffee and friendly staff!", date: "2025-01-14", likes: 12, dislikes: 1},
                    {user: "mystery_fan", rating: 5, text: "Amazing mystery section! Owner gives great recommendations.", date: "2025-01-09", likes: 9, dislikes: 0}
                ]
            },
            {
                id: 7,
                name: "Paws & Claws Pet Grooming",
                category: "Services",
                address: "222 Bark Avenue",
                phone: "(555) 789-0123",
                deal: "10% off first grooming appointment",
                reviews: [
                    {user: "dog_mom", rating: 5, text: "They treat my pup like royalty! Always come out looking adorable.", date: "2025-01-22", likes: 18, dislikes: 0},
                    {user: "cat_lady", rating: 4, text: "Great service but they don't take appointments, only walk-ins.", date: "2025-01-19", likes: 6, dislikes: 3},
                    {user: "pet_parent", rating: 5, text: "Gentle with nervous pets. Very patient and caring staff.", date: "2025-01-16", likes: 14, dislikes: 1},
                    {user: "furry_friend", rating: 2, text: "Overpriced for basic grooming. Can find cheaper elsewhere.", date: "2025-01-13", likes: 4, dislikes: 11}
                ]
            },
            {
                id: 8,
                name: "Sunset Fitness Center",
                category: "Health & Wellness",
                address: "777 Gym Boulevard",
                phone: "(555) 890-1234",
                deal: "No joining fee for January signups",
                reviews: [
                    {user: "gym_rat", rating: 4, text: "Great equipment and clean facilities. Gets busy after work.", date: "2025-01-23", likes: 11, dislikes: 3},
                    {user: "fitness_journey", rating: 5, text: "Amazing trainers! Lost 20 pounds in 3 months.", date: "2025-01-20", likes: 21, dislikes: 0},
                    {user: "cardio_king", rating: 3, text: "Decent gym but could use more cardio machines.", date: "2025-01-17", likes: 5, dislikes: 4},
                    {user: "weightlifter_x", rating: 5, text: "Best free weight section in town. Love the atmosphere!", date: "2025-01-14", likes: 16, dislikes: 2},
                    {user: "yoga_girl", rating: 4, text: "Good classes but would love more variety in yoga styles.", date: "2025-01-11", likes: 8, dislikes: 1}
                ]
            },
            {
                id: 9,
                name: "Artisan Bakery & Pastries",
                category: "Food & Dining",
                address: "444 Sweet Street",
                phone: "(555) 901-2345",
                deal: "Free cookie with coffee purchase",
                reviews: [
                    {user: "sweet_tooth", rating: 5, text: "Heaven on earth! The croissants are absolutely perfect.", date: "2025-01-24", likes: 25, dislikes: 0},
                    {user: "baker_enthusiast", rating: 5, text: "Real artisan quality. You can taste the love in every bite.", date: "2025-01-21", likes: 19, dislikes: 1},
                    {user: "breakfast_fan", rating: 4, text: "Delicious but sells out early. Get there before 10am!", date: "2025-01-18", likes: 13, dislikes: 2},
                    {user: "gluten_free_life", rating: 2, text: "Wish they had more gluten-free options.", date: "2025-01-15", likes: 7, dislikes: 9}
                ]
            },
            {
                id: 10,
                name: "Quick Cuts Hair Salon",
                category: "Services",
                address: "999 Style Avenue",
                phone: "(555) 012-3456",
                deal: "15% off all services for students",
                reviews: [
                    {user: "stylish_sue", rating: 5, text: "Best haircut I've ever had! Lisa is a magician with scissors.", date: "2025-01-23", likes: 17, dislikes: 0},
                    {user: "trendy_hair", rating: 4, text: "Good cuts but appointment wait times can be long.", date: "2025-01-20", likes: 9, dislikes: 3},
                    {user: "college_student", rating: 5, text: "Love the student discount! Always leave happy.", date: "2025-01-17", likes: 12, dislikes: 1},
                    {user: "mens_grooming", rating: 3, text: "Okay for basic cuts but nothing special.", date: "2025-01-14", likes: 4, dislikes: 6},
                    {user: "color_queen", rating: 5, text: "Amazing color work! They really listen to what you want.", date: "2025-01-10", likes: 15, dislikes: 2}
                ]
            }
        ];

        /**
         * User authentication and data storage
         * Structure: username -> { password, favorites[], reviews[], reviewInteractions{} }
         */
        let users = {
            demo: {
                password: "demo123",
                favorites: [1, 5],
                reviews: [],
                reviewInteractions: {}
            }
        };

        let currentUser = null;
        let selectedBusinessForReview = null;
        let selectedRating = 0;
        let captchaChecked = false;
        let currentFilter = 'all';
        let currentCategory = 'all';
        let allBusinesses = [...businesses];
        let activityLog = [];

        // Dark Mode
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
            const icon = document.getElementById('darkModeIcon');
            const text = document.getElementById('darkModeText');
            
            if (document.body.classList.contains('dark-mode')) {
                icon.textContent = '☀️';
                text.textContent = 'Light Mode';
                localStorage.setItem('darkMode', 'enabled');
            } else {
                icon.textContent = '🌙';
                text.textContent = 'Dark Mode';
                localStorage.setItem('darkMode', 'disabled');
            }
        }

        // Load dark mode preference
        if (localStorage.getItem('darkMode') === 'enabled') {
            document.body.classList.add('dark-mode');
            setTimeout(() => {
                document.getElementById('darkModeIcon').textContent = '☀️';
                document.getElementById('darkModeText').textContent = 'Light Mode';
            }, 100);
        }

        // Profile Toggle
        function toggleProfile() {
            const profile = document.getElementById('profileSection');
            const badges = document.getElementById('badgesSection');
            const activity = document.getElementById('activitySection');
            
            const isHidden = profile.classList.contains('hidden');
            
            profile.classList.toggle('hidden');
            badges.classList.toggle('hidden');
            activity.classList.toggle('hidden');
            
            if (isHidden) {
                updateProfileStats();
                updateBadges();
                updateActivityFeed();
            }
        }

        // Update Profile Stats
        function updateProfileStats() {
            const reviewCount = allBusinesses.reduce((count, b) => {
                return count + b.reviews.filter(r => r.user === currentUser).length;
            }, 0);
            
            const favoriteCount = users[currentUser].favorites.length;
            
            const likesGiven = Object.keys(users[currentUser].reviewInteractions).length;
            
            const badgeCount = getBadgeCount();
            
            document.getElementById('userReviewCount').textContent = reviewCount;
            document.getElementById('userFavoriteCount').textContent = favoriteCount;
            document.getElementById('userLikesGiven').textContent = likesGiven;
            document.getElementById('userBadgeCount').textContent = badgeCount;
        }

        // Badge System
        function getBadgeCount() {
            let count = 0;
            const reviewCount = allBusinesses.reduce((c, b) => {
                return c + b.reviews.filter(r => r.user === currentUser).length;
            }, 0);
            
            if (reviewCount >= 1) count++;
            if (reviewCount >= 5) count++;
            if (users[currentUser].favorites.length >= 3) count++;
            if (Object.keys(users[currentUser].reviewInteractions).length >= 10) count++;
            
            return count;
        }

        function updateBadges() {
            const reviewCount = allBusinesses.reduce((c, b) => {
                return c + b.reviews.filter(r => r.user === currentUser).length;
            }, 0);
            
            // First Review Badge
            if (reviewCount >= 1) {
                document.getElementById('badge-first-review').classList.remove('locked');
            }
            
            // 5 Reviews Badge
            if (reviewCount >= 5) {
                document.getElementById('badge-reviewer').classList.remove('locked');
            }
            
            // Explorer Badge (3+ favorites)
            if (users[currentUser].favorites.length >= 3) {
                document.getElementById('badge-explorer').classList.remove('locked');
            }
            
            // Supporter Badge (10+ likes given)
            if (Object.keys(users[currentUser].reviewInteractions).length >= 10) {
                document.getElementById('badge-supporter').classList.remove('locked');
            }
        }

        // Activity Feed
        function addActivity(text) {
            const activity = {
                text: text,
                time: new Date().toLocaleTimeString(),
                date: new Date().toLocaleDateString()
            };
            activityLog.unshift(activity);
            if (activityLog.length > 10) activityLog.pop();
        }

        function updateActivityFeed() {
            const activityList = document.getElementById('activityList');
            if (activityLog.length === 0) {
                activityList.innerHTML = '<p style="color: var(--text-secondary); text-align: center;">No recent activity</p>';
                return;
            }
            
            activityList.innerHTML = activityLog.map(a => `
                <div class="activity-item">
                    <div>${a.text}</div>
                    <div class="activity-time">${a.date} at ${a.time}</div>
                </div>
            `).join('');
        }

        // Help System
        function showHelp() {
            document.getElementById('helpModal').classList.add('active');
        }

        function closeHelpModal() {
            document.getElementById('helpModal').classList.remove('active');
        }

        // Export Report Function
        function exportReport() {
            const userReviews = [];
            allBusinesses.forEach(b => {
                b.reviews.forEach(r => {
                    if (r.user === currentUser) {
                        userReviews.push({
                            business: b.name,
                            rating: r.rating,
                            text: r.text,
                            date: r.date
                        });
                    }
                });
            });
            
            const favoriteBusinesses = allBusinesses
                .filter(b => users[currentUser].favorites.includes(b.id))
                .map(b => ({ name: b.name, category: b.category }));
            
            const report = {
                user: currentUser,
                generatedDate: new Date().toISOString(),
                statistics: {
                    totalReviews: userReviews.length,
                    totalFavorites: favoriteBusinesses.length,
                    totalLikesGiven: Object.keys(users[currentUser].reviewInteractions).length,
                    badgesEarned: getBadgeCount()
                },
                reviews: userReviews,
                favorites: favoriteBusinesses,
                recentActivity: activityLog,
                preferences: {
                    darkMode: document.body.classList.contains('dark-mode')
                }
            };
            
            const dataStr = JSON.stringify(report, null, 2);
            const dataBlob = new Blob([dataStr], { type: 'application/json' });
            const url = URL.createObjectURL(dataBlob);
            
            const link = document.createElement('a');
            link.href = url;
            link.download = `TownSquare_Report_${currentUser}_${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            addActivity('📊 Exported activity report');
            alert('✅ Report exported successfully!');
        }

        // Category Filter
        function filterByCategory(category) {
            currentCategory = category;
            
            // Update active category pill
            document.querySelectorAll('.category-pill').forEach(pill => {
                pill.classList.remove('active');
            });
            event.target.classList.add('active');
            
            applyCurrentFilter();
        }

        // Disclaimer
        function acceptDisclaimer() {
            document.getElementById('disclaimerOverlay').classList.add('hidden');
        }

        // Auth
        function switchAuthTab(tab) {
            const tabs = document.querySelectorAll('.auth-tab');
            tabs.forEach(t => t.classList.remove('active'));
            
            if (tab === 'login') {
                tabs[0].classList.add('active');
                document.getElementById('loginForm').classList.remove('hidden');
                document.getElementById('registerForm').classList.add('hidden');
            } else {
                tabs[1].classList.add('active');
                document.getElementById('loginForm').classList.add('hidden');
                document.getElementById('registerForm').classList.remove('hidden');
            }
        }

        function login() {
            const username = document.getElementById('loginUsername').value.trim();
            const password = document.getElementById('loginPassword').value;

            if (!username || !password) {
                alert('Please enter both username and password');
                return;
            }

            if (users[username] && users[username].password === password) {
                currentUser = username;
                document.getElementById('currentUser').textContent = username;
                document.getElementById('authSection').classList.add('hidden');
                document.getElementById('appContainer').classList.add('active');
                
                // Show browse section by default
                switchTab('browse');
                
                // Trigger animations for stats and taskbar
                setTimeout(() => {
                    triggerScrollAnimations();
                }, 100);
            } else {
                alert('❌ Invalid credentials');
            }
        }

        function register() {
            const username = document.getElementById('regUsername').value.trim();
            const password = document.getElementById('regPassword').value;

            if (!username || !password) {
                alert('Please fill in all fields');
                return;
            }

            if (password.length < 4) {
                alert('Password must be at least 4 characters');
                return;
            }

            if (users[username]) {
                alert('Username already exists');
                return;
            }

            users[username] = {
                password: password,
                favorites: [],
                reviews: [],
                reviewInteractions: {}
            };

            alert('✅ Account created! Please login.');
            switchAuthTab('login');
        }

        function logout() {
            currentUser = null;
            document.getElementById('appContainer').classList.remove('active');
            document.getElementById('authSection').classList.remove('hidden');
            document.getElementById('loginUsername').value = '';
            document.getElementById('loginPassword').value = '';
        }

        // Business Functions
        function getAverageRating(business) {
            if (business.reviews.length === 0) return 0;
            const sum = business.reviews.reduce((acc, r) => acc + r.rating, 0);
            return (sum / business.reviews.length).toFixed(1);
        }

        function getReviewStats(business) {
            let positive = 0;
            let negative = 0;
            business.reviews.forEach(r => {
                if (r.rating >= 4) positive++;
                else if (r.rating <= 2) negative++;
            });
            return { positive, negative };
        }

        function getReviewId(businessId, reviewIndex) {
            return `${businessId}-${reviewIndex}`;
        }

        function renderBusinessCard(business) {
            const avg = getAverageRating(business);
            const isFavorite = users[currentUser].favorites.includes(business.id);
            const stars = avg > 0 ? '⭐'.repeat(Math.round(avg)) : 'No ratings yet';
            const stats = getReviewStats(business);

            return `
                <div class="business-card">
                    <div class="business-header">
                        <div class="business-name">${business.name}</div>
                        <span class="business-category">${business.category}</span>
                    </div>
                    <div class="business-body">
                        <div class="rating">${stars} ${avg > 0 ? avg : ''}</div>
                        <div class="review-stats">
                            <span class="stat-positive">👍 ${stats.positive} positive</span>
                            <span class="stat-negative">👎 ${stats.negative} negative</span>
                        </div>
                        <div class="business-info">
                            <div class="info-row">📍 ${business.address}</div>
                            <div class="info-row">📞 ${business.phone}</div>
                        </div>
                        <div class="deal-badge">💰 ${business.deal}</div>
                        ${business.reviews.length > 0 ? `
                            <div style="margin-top: 1rem;">
                                <strong style="color: var(--deep-teal);">Recent Reviews:</strong>
                                ${business.reviews.slice(-2).map((r, idx) => {
                                    const reviewId = getReviewId(business.id, business.reviews.length - 2 + idx);
                                    const userInteraction = users[currentUser].reviewInteractions[reviewId];
                                    return `
                                    <div class="review-item">
                                        <div class="review-header">
                                            <span class="review-user">${r.user}</span>
                                            <span>${'⭐'.repeat(r.rating)}</span>
                                        </div>
                                        <div>${r.text}</div>
                                        <div class="review-actions">
                                            <button class="review-action-btn ${userInteraction === 'like' ? 'liked' : ''}" 
                                                    onclick="likeReview(${business.id}, ${business.reviews.length - 2 + idx})">
                                                👍 ${r.likes}
                                            </button>
                                            <button class="review-action-btn ${userInteraction === 'dislike' ? 'disliked' : ''}" 
                                                    onclick="dislikeReview(${business.id}, ${business.reviews.length - 2 + idx})">
                                                👎 ${r.dislikes}
                                            </button>
                                        </div>
                                    </div>
                                `}).join('')}
                            </div>
                        ` : '<p style="color: #666; text-align: center; margin: 1rem 0;">No reviews yet. Be the first!</p>'}
                        <div class="business-actions">
                            <button class="btn btn-primary btn-small" onclick="openReviewModal(${business.id})">
                                ✍️ Review
                            </button>
                            <button class="btn btn-secondary btn-small" onclick="toggleFavorite(${business.id})">
                                ${isFavorite ? '💙 Favorited' : '🤍 Favorite'}
                            </button>
                        </div>
                    </div>
                </div>
            `;
        }

        function renderBusinesses(businessList, containerId) {
            const container = document.getElementById(containerId);
            if (businessList.length === 0) {
                container.innerHTML = `
                    <div class="empty-state">
                        <div class="empty-icon">🏪</div>
                        <h3>No businesses found</h3>
                        <p>Try adjusting your search or filters</p>
                    </div>
                `;
                return;
            }
            container.innerHTML = businessList.map(renderBusinessCard).join('');
        }

        // Review Interactions
        function likeReview(businessId, reviewIndex) {
            const business = allBusinesses.find(b => b.id === businessId);
            const review = business.reviews[reviewIndex];
            const reviewId = getReviewId(businessId, reviewIndex);
            const currentInteraction = users[currentUser].reviewInteractions[reviewId];

            if (currentInteraction === 'like') {
                review.likes--;
                delete users[currentUser].reviewInteractions[reviewId];
            } else {
                if (currentInteraction === 'dislike') {
                    review.dislikes--;
                }
                review.likes++;
                users[currentUser].reviewInteractions[reviewId] = 'like';
            }

            refreshCurrentView();
        }

        function dislikeReview(businessId, reviewIndex) {
            const business = allBusinesses.find(b => b.id === businessId);
            const review = business.reviews[reviewIndex];
            const reviewId = getReviewId(businessId, reviewIndex);
            const currentInteraction = users[currentUser].reviewInteractions[reviewId];

            if (currentInteraction === 'dislike') {
                review.dislikes--;
                delete users[currentUser].reviewInteractions[reviewId];
            } else {
                if (currentInteraction === 'like') {
                    review.likes--;
                }
                review.dislikes++;
                users[currentUser].reviewInteractions[reviewId] = 'dislike';
            }

            refreshCurrentView();
        }

        function refreshCurrentView() {
            const activeSection = document.querySelector('.content-section.active');
            if (activeSection.id === 'browseSection') {
                applyCurrentFilter();
            } else if (activeSection.id === 'favoritesSection') {
                showSection('favorites');
            }
        }

        // Filter Functions
        function filterReviews(type, buttonElement) {
            currentFilter = type;
            
            // Update button states - remove active from all, add to clicked
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Add active class based on type
            const filterButtons = {
                'all': 0,
                'positive': 1,
                'negative': 2,
                'highly-rated': 3
            };
            
            const buttons = document.querySelectorAll('.filter-btn');
            if (buttons[filterButtons[type]]) {
                buttons[filterButtons[type]].classList.add('active');
            }

            applyCurrentFilter();
        }

        function applyCurrentFilter() {
            let filtered = [...allBusinesses];
            console.log('Starting filter. Total businesses:', filtered.length);
            console.log('Current filter:', currentFilter);
            console.log('Current category:', currentCategory);

            // Apply category filter first
            if (currentCategory !== 'all') {
                filtered = filtered.filter(b => b.category === currentCategory);
                console.log('After category filter:', filtered.length);
            }

            if (currentFilter === 'positive') {
                filtered = filtered.filter(b => {
                    const stats = getReviewStats(b);
                    return stats.positive > stats.negative && stats.positive > 0;
                });
                console.log('After positive filter:', filtered.length);
            } else if (currentFilter === 'negative') {
                filtered = filtered.filter(b => {
                    const stats = getReviewStats(b);
                    return stats.negative > 0;
                });
                console.log('After negative filter:', filtered.length);
            } else if (currentFilter === 'highly-rated') {
                filtered = filtered.filter(b => parseFloat(getAverageRating(b)) >= 4);
                console.log('After highly-rated filter:', filtered.length);
            }

            const searchQuery = document.getElementById('searchInput').value.toLowerCase();
            if (searchQuery) {
                filtered = filtered.filter(b => 
                    b.name.toLowerCase().includes(searchQuery) || 
                    b.category.toLowerCase().includes(searchQuery)
                );
                console.log('After search filter:', filtered.length);
            }

            console.log('Rendering businesses:', filtered.length);
            renderBusinesses(filtered, 'businessGrid');
        }

        function showSection(section) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
            
            const sectionMap = {
                'browse': 'browseSection',
                'favorites': 'favoritesSection',
                'deals': 'dealsSection',
                'recommendations': 'recommendationsSection'
            };
            
            document.getElementById(sectionMap[section]).classList.add('active');

            if (section === 'browse') {
                applyCurrentFilter();
            } else if (section === 'favorites') {
                const favs = allBusinesses.filter(b => users[currentUser].favorites.includes(b.id));
                renderBusinesses(favs, 'favoritesGrid');
            } else if (section === 'deals') {
                renderBusinesses(allBusinesses, 'dealsGrid');
            } else if (section === 'recommendations') {
                const recommendations = getRecommendations();
                renderBusinesses(recommendations, 'recommendationsGrid');
            }

            // Trigger scroll animations for new content
            triggerScrollAnimations();
        }

        function switchTab(section) {
            // Update active tab styling
            document.querySelectorAll('.nav-tab-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            
            const activeBtn = document.querySelector(`[data-section="${section}"]`);
            if (activeBtn) {
                activeBtn.classList.add('active');
            }

            // Show the section
            showSection(section);
        }

        function sortByRating() {
            // Get currently displayed businesses and sort them
            let currentBusinesses = [...allBusinesses];
            
            // Apply current filter first
            if (currentFilter === 'positive') {
                currentBusinesses = currentBusinesses.filter(b => {
                    const stats = getReviewStats(b);
                    return stats.positive > stats.negative && stats.positive > 0;
                });
            } else if (currentFilter === 'negative') {
                currentBusinesses = currentBusinesses.filter(b => {
                    const stats = getReviewStats(b);
                    return stats.negative > 0;
                });
            } else if (currentFilter === 'highly-rated') {
                currentBusinesses = currentBusinesses.filter(b => parseFloat(getAverageRating(b)) >= 4);
            }
            
            // Apply search if active
            const searchQuery = document.getElementById('searchInput').value.toLowerCase();
            if (searchQuery) {
                currentBusinesses = currentBusinesses.filter(b => 
                    b.name.toLowerCase().includes(searchQuery) || 
                    b.category.toLowerCase().includes(searchQuery)
                );
            }
            
            // Now sort
            currentBusinesses.sort((a, b) => {
                const avgA = parseFloat(getAverageRating(a)) || 0;
                const avgB = parseFloat(getAverageRating(b)) || 0;
                return avgB - avgA;
            });
            
            renderBusinesses(currentBusinesses, 'businessGrid');
        }

        function searchBusinesses() {
            applyCurrentFilter();
        }

        function toggleFavorite(businessId) {
            const favs = users[currentUser].favorites;
            const index = favs.indexOf(businessId);
            const business = allBusinesses.find(b => b.id === businessId);
            
            if (index > -1) {
                favs.splice(index, 1);
                addActivity(`Removed ${business.name} from favorites`);
            } else {
                favs.push(businessId);
                addActivity(`Added ${business.name} to favorites ❤️`);
            }
            
            refreshCurrentView();
        }

        function getRecommendations() {
            const favs = users[currentUser].favorites;
            if (favs.length === 0) return [];

            const categories = {};
            allBusinesses.forEach(b => {
                if (favs.includes(b.id)) {
                    categories[b.category] = (categories[b.category] || 0) + 1;
                }
            });

            const topCategory = Object.keys(categories).reduce((a, b) => 
                categories[a] > categories[b] ? a : b
            );

            return allBusinesses.filter(b => 
                b.category === topCategory && !favs.includes(b.id)
            );
        }

        // Review Modal & CAPTCHA
        function openReviewModal(businessId) {
            selectedBusinessForReview = businessId;
            const business = allBusinesses.find(b => b.id === businessId);
            document.getElementById('reviewBusinessName').textContent = business.name;
            document.getElementById('reviewModal').classList.add('active');
            selectedRating = 0;
            captchaChecked = false;
            document.getElementById('reviewText').value = '';
            document.getElementById('captchaCheckbox').classList.remove('checked');
            document.getElementById('captchaCheck').classList.add('hidden');
            updateStarDisplay();
        }

        function closeReviewModal() {
            document.getElementById('reviewModal').classList.remove('active');
        }

        function toggleCaptcha() {
            captchaChecked = !captchaChecked;
            const checkbox = document.getElementById('captchaCheckbox');
            const check = document.getElementById('captchaCheck');
            
            if (captchaChecked) {
                checkbox.classList.add('checked');
                check.classList.remove('hidden');
            } else {
                checkbox.classList.remove('checked');
                check.classList.add('hidden');
            }
        }

        function setRating(rating) {
            selectedRating = rating;
            updateStarDisplay();
        }

        function updateStarDisplay() {
            const stars = document.querySelectorAll('.star');
            stars.forEach((star, index) => {
                if (index < selectedRating) {
                    star.classList.add('active');
                } else {
                    star.classList.remove('active');
                }
            });
        }

        function submitReview() {
            if (!captchaChecked) {
                alert('⚠️ Please verify that you are not a robot');
                return;
            }

            if (selectedRating === 0) {
                alert('⚠️ Please select a rating');
                return;
            }

            const text = document.getElementById('reviewText').value.trim();
            if (!text) {
                alert('⚠️ Please write a review');
                return;
            }

            const business = allBusinesses.find(b => b.id === selectedBusinessForReview);
            
            business.reviews = business.reviews.filter(r => r.user !== currentUser);
            
            business.reviews.push({
                user: currentUser,
                rating: selectedRating,
                text: text,
                date: new Date().toISOString().split('T')[0],
                likes: 0,
                dislikes: 0
            });

            addActivity(`Reviewed ${business.name} - ${selectedRating}⭐`);
            
            alert('✅ Review submitted successfully!');
            closeReviewModal();
            refreshCurrentView();
        }

        // Scroll Animation Observer
        function initScrollAnimations() {
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        
                        // Trigger counter animation for stats
                        if (entry.target.classList.contains('stat-item')) {
                            animateStatNumber(entry.target);
                        }
                    }
                });
            }, observerOptions);

            // Observe all animatable elements
            const animateOnScroll = () => {
                const elements = document.querySelectorAll(
                    '.business-card, .nav-taskbar, .filter-controls, .search-bar, .section-header, .stat-item'
                );
                elements.forEach(el => observer.observe(el));
            };

            // Run initially and after any content update
            animateOnScroll();
            
            // Re-observe when content changes
            window.addEventListener('contentUpdated', animateOnScroll);
        }

        // Animate stat numbers
        function animateStatNumber(statItem) {
            const numberEl = statItem.querySelector('.stat-number');
            if (!numberEl || numberEl.dataset.animated) return;
            
            numberEl.dataset.animated = 'true';
            const targetText = numberEl.textContent;
            const hasPlus = targetText.includes('+');
            const targetNum = parseInt(targetText.replace(/\D/g, ''));
            
            if (isNaN(targetNum)) return;
            
            let current = 0;
            const increment = targetNum / 30;
            const timer = setInterval(() => {
                current += increment;
                if (current >= targetNum) {
                    numberEl.textContent = targetNum + (hasPlus ? '+' : '');
                    clearInterval(timer);
                } else {
                    numberEl.textContent = Math.floor(current) + (hasPlus ? '+' : '');
                }
            }, 50);
        }

        // Trigger scroll animations when showing sections
        function triggerScrollAnimations() {
            setTimeout(() => {
                const event = new Event('contentUpdated');
                window.dispatchEvent(event);
                initScrollAnimations();
            }, 100);
        }

        // Initialize on page load
        window.addEventListener('load', () => {
            initScrollAnimations();
        });
    </script>
</body>
</html>