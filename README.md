<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Byte-Sized Business Boost | FBLA 2026</title>
    <style>
        /* CSS variables for consistent design rationale [cite: 121, 194] */
        :root {
            --primary: #1e40af;
            --secondary: #0ea5e9;
            --accent: #f59e0b;
            --success: #10b981;
            --danger: #ef4444;
            --bg-light: #f8fafc;
            --text-dark: #0f172a;
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }

        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            margin: 0;
            line-height: 1.5;
        }

        /* Accessibility focus [cite: 122, 195] */
        .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); border: 0; }

        .container { max-width: 1100px; margin: 0 auto; padding: 2rem; }

        /* UI/UX Components [cite: 123, 196] */
        header { text-align: center; margin-bottom: 3rem; }
        .hero { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; padding: 3rem; border-radius: 1rem; box-shadow: var(--shadow); }

        .auth-barrier {
            background: white;
            padding: 2rem;
            border-radius: 0.75rem;
            max-width: 400px;
            margin: 2rem auto;
            text-align: center;
            border: 2px solid var(--accent);
        }

        .tool-bar {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
            background: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: var(--shadow);
        }

        .business-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1.5rem;
        }

        .biz-card {
            background: white;
            border-radius: 0.75rem;
            overflow: hidden;
            transition: transform 0.2s;
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
        }

        .biz-card:hover { transform: translateY(-5px); box-shadow: var(--shadow); }
        .biz-content { padding: 1.5rem; flex-grow: 1; }
        
        .badge { font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; border-radius: 999px; text-transform: uppercase; }
        .badge-food { background: #fee2e2; color: #991b1b; }
        .badge-retail { background: #fef3c7; color: #92400e; }
        .badge-services { background: #dcfce7; color: #166534; }

        .rating-stars { color: var(--accent); font-weight: bold; }
        
        .coupon-box {
            background: #fffbeb;
            border: 2px dashed var(--accent);
            padding: 0.75rem;
            margin: 1rem 0;
            border-radius: 0.5rem;
            text-align: center;
        }

        .stats-panel {
            background: #1e293b;
            color: white;
            padding: 2rem;
            border-radius: 1rem;
            margin-top: 3rem;
        }

        button {
            cursor: pointer;
            border: none;
            border-radius: 0.5rem;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            transition: opacity 0.2s;
        }

        .btn-primary { background: var(--primary); color: white; }
        .btn-outline { border: 1px solid var(--primary); color: var(--primary); background: transparent; }
        .btn-fav { background: #fff1f2; color: #be123c; width: 100%; margin-top: 1rem; }
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="hero">
            <h1>Byte-Sized Business Boost</h1>
            <p>Empowering Local Entrepreneurs through Technology</p>
        </div>
    </header>

    <div id="security-check" class="auth-barrier">
        <h3>Security Verification</h3>
        <p>Please solve this logic puzzle to access local coupons:</p>
        <p id="captcha-question" style="font-weight: bold; font-size: 1.2rem;"></p>
        <input type="number" id="captcha-input" placeholder="Your Answer" style="width: 80%; padding: 0.5rem; margin-bottom: 1rem;">
        <br>
        <button onclick="App.verifyBot()" class="btn-primary">Access Deals</button>
    </div>

    <main id="main-app" class="sr-only">
        <section id="recommendation-banner" style="margin-bottom: 2rem;"></section>

        <div class="tool-bar">
            <div>
                <label for="filter-category">Category</label>
                <select id="filter-category" onchange="App.handleFilterChange()">
                    <option value="all">All Industries</option>
                    <option value="food">Food & Dining</option>
                    <option value="retail">Retail</option>
                    <option value="services">Technical Services</option>
                </select>
            </div>
            <div>
                <label for="sort-logic">Rank By</label>
                <select id="sort-logic" onchange="App.handleFilterChange()">
                    <option value="name">Alphabetical</option>
                    <option value="rating">Highest Rated</option>
                </select>
            </div>
            <div style="display: flex; align-items: flex-end;">
                <button onclick="App.generateDataReport()" class="btn-outline">📊 View Community Impact Report</button>
            </div>
        </div>

        <div id="business-grid" class="business-grid">
            </div>

        <div id="report-output" class="stats-panel sr-only">
            <h3>Community Data Analysis</h3>
            <div id="report-content"></div>
            <button onclick="document.getElementById('report-output').classList.add('sr-only')" class="btn-outline" style="color: white; border-color: white; margin-top: 1rem;">Close Report</button>
        </div>
    </main>
</div>

<script>
/**
 * FBLA CODING & PROGRAMMING 2026
 * Topic: Byte-Sized Business Boost
 * * DESIGN RATIONALE[cite: 116, 189]:
 * Using Object-Oriented JavaScript to ensure modularity and scalability.
 * This approach separates Data (Model), Logic (Controller), and UI (View).
 */

const App = (() => {
    // 1. DATA STORE (The "Model") 
    const state = {
        businesses: [
            { id: 1, name: "The Caffeine Patch", category: "food", rating: 4.9, reviews: 128, deal: "Free Cookie with Large Latte", bookmarked: false },
            { id: 2, name: "Byte-Scale Repair", category: "services", rating: 4.7, reviews: 85, deal: "15% off Screen Replacement", bookmarked: false },
            { id: 3, name: "Main Street Books", category: "retail", rating: 4.5, reviews: 210, deal: "BOGO on Used Hardcovers", bookmarked: false },
            { id: 4, name: "Green Thumb Garden", category: "retail", rating: 4.2, reviews: 45, deal: "Free Bag of Soil with any Plant", bookmarked: false },
            { id: 5, name: "Binary Bistro", category: "food", rating: 4.8, reviews: 312, deal: "50% off Appetizers after 8PM", bookmarked: false }
        ],
        captcha: { q: "", a: 0 }
    };

    // 2. LOGIC (The "Controller") [cite: 120, 193]
    const init = () => {
        generateCaptcha();
        render();
    };

    const generateCaptcha = () => {
        const n1 = Math.floor(Math.random() * 10) + 1;
        const n2 = Math.floor(Math.random() * 10) + 1;
        state.captcha.q = `What is ${n1} plus ${n2}?`;
        state.captcha.a = n1 + n2;
        document.getElementById('captcha-question').innerText = state.captcha.q;
    };

    const verifyBot = () => {
        const userInput = parseInt(document.getElementById('captcha-input').value);
        // Input Validation [cite: 126, 199]
        if (isNaN(userInput)) {
            alert("Error: Please enter a numeric value.");
            return;
        }
        if (userInput === state.captcha.a) {
            document.getElementById('security-check').classList.add('sr-only');
            document.getElementById('main-app').classList.remove('sr-only');
            updateRecommendation();
        } else {
            alert("Verification failed. Robots are not permitted.");
            generateCaptcha();
        }
    };

    const updateRecommendation = () => {
        // Intelligent Feature Logic [cite: 124, 197]
        const topBiz = [...state.businesses].sort((a, b) => b.rating - a.rating)[0];
        const banner = document.getElementById('recommendation-banner');
        banner.innerHTML = `
            <div style="background: #ecfdf5; border: 1px solid #10b981; padding: 1rem; border-radius: 0.5rem;">
                <strong>💡 Smart Recommendation:</strong> Based on community feedback, 
                we suggest visiting <strong>${topBiz.name}</strong>, currently rated at ${topBiz.rating} stars!
            </div>
        `;
    };

    // 3. UI RENDERING (The "View") [cite: 127, 200]
    const render = () => {
        const catFilter = document.getElementById('filter-category').value;
        const sortLogic = document.getElementById('sort-logic').value;
        const grid = document.getElementById('business-grid');

        let displayList = state.businesses.filter(b => catFilter === 'all' || b.category === catFilter);

        displayList.sort((a, b) => {
            if (sortLogic === 'rating') return b.rating - a.rating;
            return a.name.localeCompare(b.name);
        });

        grid.innerHTML = displayList.map(biz => `
            <article class="biz-card">
                <div class="biz-content">
                    <span class="badge badge-${biz.category}">${biz.category}</span>
                    <h3 style="margin: 0.5rem 0;">${biz.name}</h3>
                    <div class="rating-stars">⭐ ${biz.rating} <span style="color: #64748b; font-weight: normal; font-size: 0.8rem;">(${biz.reviews} reviews)</span></div>
                    
                    <div class="coupon-box">
                        <small>PROMO CODE: LOCAL2026</small>
                        <div style="font-weight: bold; color: var(--primary);">${biz.deal}</div>
                    </div>
                    
                    <button onclick="App.toggleFav(${biz.id})" class="btn-fav">
                        ${biz.bookmarked ? '❤️ Saved to Favorites' : '🤍 Bookmark Business'}
                    </button>
                </div>
            </article>
        `).join('');
    };

    const toggleFav = (id) => {
        const biz = state.businesses.find(b => b.id === id);
        if (biz) {
            biz.bookmarked = !biz.bookmarked;
            render();
        }
    };

    const generateDataReport = () => {
        const reportPanel = document.getElementById('report-output');
        const content = document.getElementById('report-content');
        
        // Data Analysis Logic [cite: 128, 201]
        const avg = state.businesses.reduce((acc, b) => acc + b.rating, 0) / state.businesses.length;
        const totalReviews = state.businesses.reduce((acc, b) => acc + b.reviews, 0);
        const favCount = state.businesses.filter(b => b.bookmarked).length;

        reportPanel.classList.remove('sr-only');
        content.innerHTML = `
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; text-align: center;">
                <div><h4>Average Rating</h4><p style="font-size: 2rem;">${avg.toFixed(2)}</p></div>
                <div><h4>Total Community Engagement</h4><p style="font-size: 2rem;">${totalReviews}</p></div>
                <div><h4>Your Bookmarks</h4><p style="font-size: 2rem;">${favCount}</p></div>
            </div>
            <p style="margin-top: 2rem; color: #94a3b8;">This report uses real-time data from the current session's state management system to analyze local business performance.</p>
        `;
    };

    return {
        init,
        verifyBot,
        handleFilterChange: render,
        toggleFav,
        generateDataReport
    };
})();

// Initialize Application on Load
window.onload = App.init;
</script>
</body>
</html>