<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TownSquare - Your Local Business Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        /* --- CORE THEME & RESET --- */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        :root {
            --sunset-orange: #FF6B35; --deep-teal: #004E64; --warm-cream: #FFF8F0;
            --soft-coral: #FF9F80; --midnight: #1A2332; --golden: #F7B32B;
            --shadow: rgba(0, 78, 100, 0.15); --success-green: #10B981; --danger-red: #EF4444;
            --bg-primary: #f8f9fa; --bg-secondary: #e9ecef; --text-primary: #1A2332;
            --text-secondary: #666; --card-bg: white;
        }
        body.dark-mode {
            --bg-primary: #1a1a2e; --bg-secondary: #16213e; --text-primary: #eee;
            --text-secondary: #aaa; --card-bg: #0f3460;
        }
        body {
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
            color: var(--text-primary);
            min-height: 100vh;
            transition: background 0.3s ease, color 0.3s ease;
        }

        /* --- FBLA DISCLAIMER OVERLAY --- */
        #disclaimerOverlay {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.95); z-index: 10000;
            display: flex; align-items: center; justify-content: center;
            backdrop-filter: blur(10px);
        }
        .disclaimer-content {
            background: white; padding: 3rem; border-radius: 20px;
            max-width: 600px; width: 90%; text-align: center; color: #1A2332;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        }
        .fbla-banner {
            background: #003DA5; color: white; padding: 0.8rem;
            text-align: center; font-weight: bold; position: sticky; top: 0; z-index: 999;
        }

        /* --- UI COMPONENTS --- */
        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
        .hero-section {
            background: white; border-radius: 25px; padding: 4rem 2rem;
            text-align: center; box-shadow: 0 10px 40px var(--shadow); margin-bottom: 3rem;
        }
        h1 { font-family: 'DM Serif Display', serif; font-size: 4rem; color: var(--deep-teal); }

        .auth-container { background: var(--card-bg); padding: 2.5rem; border-radius: 20px; max-width: 450px; margin: 0 auto 3rem; box-shadow: 0 20px 50px var(--shadow); }
        .auth-toggle { display: flex; gap: 1rem; margin-bottom: 2rem; }
        .auth-tab { flex: 1; padding: 0.8rem; border: none; border-radius: 10px; cursor: pointer; font-weight: 700; background: #eee; }
        .auth-tab.active { background: var(--sunset-orange); color: white; }
        
        .user-bar { background: var(--deep-teal); color: white; padding: 1.5rem; border-radius: 15px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
        .nav-taskbar { background: white; padding: 1rem; border-radius: 15px; display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem; box-shadow: 0 5px 15px var(--shadow); flex-wrap: wrap; }
        .nav-btn { padding: 0.8rem 1.5rem; border: none; border-radius: 10px; cursor: pointer; font-weight: 600; background: transparent; transition: 0.3s; }
        .nav-btn.active { background: var(--sunset-orange); color: white; }
        
        .business-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2rem; }
        .business-card { background: var(--card-bg); border-radius: 20px; overflow: hidden; box-shadow: 0 10px 25px var(--shadow); border-top: 6px solid var(--sunset-orange); }
        .card-header { padding: 1.5rem; background: rgba(0,0,0,0.03); }
        .card-body { padding: 1.5rem; }

        .modal { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: none; align-items: center; justify-content: center; z-index: 11000; }
        .modal.active { display: flex; }
        .modal-content { background: white; padding: 2.5rem; border-radius: 20px; width: 90%; max-width: 550px; color: #333; }

        .hidden { display: none !important; }
        .btn { padding: 0.8rem 1.5rem; border: none; border-radius: 10px; cursor: pointer; font-weight: 700; transition: 0.3s; }
        .btn-primary { background: var(--sunset-orange); color: white; width: 100%; }
        .btn-outline { border: 2px solid var(--deep-teal); color: var(--deep-teal); background: transparent; }
    </style>
</head>
<body>

    <div id="disclaimerOverlay">
        <div class="disclaimer-content">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🏆</div>
            <h1 style="color: #003DA5; margin-bottom: 1rem;">FBLA Educational Project</h1>
            <p style="margin-bottom: 1.5rem; line-height: 1.6;">This website is a student project created for the <strong>Future Business Leaders of America</strong>. All data, reviews, and business profiles are entirely fictional.</p>
            <button class="btn btn-primary" onclick="acceptDisclaimer()">I Understand & Enter</button>
        </div>
    </div>

    <div class="fbla-banner">DEMONSTRATION SITE — ALL CONTENT IS SIMULATED FOR EDUCATIONAL PURPOSES</div>

    <div class="container">
        <div class="hero-section" id="hero">
            <h1>TownSquare</h1>
            <p style="font-size: 1.2rem; color: var(--text-secondary);">Connecting our community, one local gem at a time.</p>
        </div>

        <div id="authContainer" class="auth-container">
            <div class="auth-toggle">
                <button class="auth-tab active" onclick="toggleAuth('login')">Login</button>
                <button class="auth-tab" onclick="toggleAuth('register')">Register</button>
            </div>
            <div id="loginForm">
                <input type="text" id="userIn" placeholder="Username (demo)" style="width:100%; padding:12px; margin-bottom:12px; border:2px solid #ddd; border-radius:10px;">
                <input type="password" id="passIn" placeholder="Password (demo123)" style="width:100%; padding:12px; margin-bottom:12px; border:2px solid #ddd; border-radius:10px;">
                <button class="btn btn-primary" onclick="app.login()">Login</button>
            </div>
        </div>

        <div id="appInterface" class="hidden">
            <div class="user-bar">
                <div style="font-size: 1.3rem;">Welcome back, <strong id="userName">User</strong>!</div>
                <div style="display:flex; gap: 10px;">
                    <button class="btn btn-outline" style="color:white; border-color:white;" onclick="app.toggleTheme()">🌙 Theme</button>
                    <button class="btn btn-outline" style="color:white; border-color:white;" onclick="app.logout()">Logout</button>
                </div>
            </div>

            <div class="nav-taskbar" style="justify-content: space-around; background: var(--warm-cream);">
                <div>Reviews: <span id="pReviews" style="font-weight:bold; color:var(--sunset-orange);">0</span></div>
                <div>Favorites: <span id="pFavs" style="font-weight:bold; color:var(--deep-teal);">0</span></div>
                <div id="badgeStatus" style="font-weight:bold; color:var(--golden);">Badges: 0</div>
            </div>

            <div class="nav-taskbar">
                <button class="nav-btn active" onclick="app.switchTab('all', this)">All Businesses</button>
                <button class="nav-btn" onclick="app.switchTab('Food & Dining', this)">Dining</button>
                <button class="nav-btn" onclick="app.switchTab('Services', this)">Services</button>
                <button class="nav-btn" onclick="app.switchTab('favs', this)">💙 My Favorites</button>
            </div>

            <div id="bizGrid" class="business-grid"></div>
        </div>
    </div>

    <div id="reviewModal" class="modal">
        <div class="modal-content">
            <h2 id="modalTitle">Write a Review</h2>
            <div style="margin: 1.5rem 0;">
                <label>Rating:</label>
                <select id="ratingIn" style="width:100%; padding:12px; border-radius:10px; margin-top:5px;">
                    <option value="5">⭐⭐⭐⭐⭐ (Excellent)</option>
                    <option value="4">⭐⭐⭐⭐ (Good)</option>
                    <option value="3">⭐⭐⭐ (Average)</option>
                    <option value="2">⭐⭐ (Poor)</option>
                    <option value="1">⭐ (Terrible)</option>
                </select>
            </div>
            <textarea id="reviewText" placeholder="Describe your experience..." style="width:100%; height:120px; padding:12px; border-radius:10px; border:2px solid #ddd;"></textarea>
            <div style="margin-top: 1.5rem; display: flex; gap: 10px;">
                <button class="btn btn-primary" onclick="app.submitReview()">Submit</button>
                <button class="btn btn-outline" onclick="app.closeModal()" style="width:100%;">Cancel</button>
            </div>
        </div>
    </div>

    <script>
        /* --- GLOBAL UI HANDLERS --- */
        function acceptDisclaimer() {
            const overlay = document.getElementById('disclaimerOverlay');
            overlay.style.opacity = '0';
            overlay.style.transition = 'opacity 0.4s ease';
            setTimeout(() => overlay.style.display = 'none', 400);
        }

        function toggleAuth(type) {
            document.querySelectorAll('.auth-tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
        }

        /* --- DATA & LOGIC --- */
        const businesses = [
            { id: 1, name: "The Morning Brew Café", category: "Food & Dining", address: "123 Main St", phone: "(555) 123-4567", deal: "Free Cookie with Large Coffee" },
            { id: 2, name: "TechRepair Pro", category: "Services", address: "456 Oak Ave", phone: "(555) 987-6543", deal: "10% Off Screen Replacement" },
            { id: 3, name: "Green Valley Grocery", category: "Food & Dining", address: "789 Pine Rd", phone: "(555) 246-8101", deal: "$5 Off $50 Organic Haul" },
            { id: 4, name: "Zen Yoga Studio", category: "Services", address: "321 Wellness Way", phone: "(555) 111-2222", deal: "First Class Free for Locals" },
            { id: 5, name: "Bella's Italian Kitchen", category: "Food & Dining", address: "555 Pasta Lane", phone: "(555) 333-4444", deal: "Half-Price Wine Wednesdays" },
            { id: 6, name: "Paws & Claws Grooming", category: "Services", address: "888 Bark Blvd", phone: "(555) 555-1212", deal: "Free Nail Trim with Groom" },
            { id: 7, name: "Blue Ribbon Hardware", category: "Services", address: "101 Fixer Upper St", phone: "(555) 666-7777", deal: "Key Duplication BOGO" },
            { id: 8, name: "Sunset Auto Body", category: "Services", address: "202 Gearhead Rd", phone: "(555) 888-9999", deal: "Free Diagnostic Checkup" },
            { id: 9, name: "The Book Nook", category: "Food & Dining", address: "303 Chapter Dr", phone: "(555) 000-1111", deal: "B2G1 Free Paperbacks" },
            { id: 10, name: "Crimson Fitness", category: "Services", address: "404 Sweat St", phone: "(555) 222-3333", deal: "$0 Enrollment This Month" }
        ];

        const app = {
            user: null,
            favorites: [],
            reviews: 0,
            activeBizId: null,

            login: function() {
                const u = document.getElementById('userIn').value;
                const p = document.getElementById('passIn').value;
                if(u === 'demo' && p === 'demo123') {
                    this.user = u;
                    document.getElementById('userName').innerText = u;
                    document.getElementById('authContainer').classList.add('hidden');
                    document.getElementById('appInterface').classList.remove('hidden');
                    this.render('all');
                } else {
                    alert("DEMO ACCOUNT: Use 'demo' and 'demo123'");
                }
            },

            logout: function() { location.reload(); },

            toggleTheme: function() { document.body.classList.toggle('dark-mode'); },

            switchTab: function(cat, btn) {
                document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.render(cat);
            },

            render: function(cat) {
                const grid = document.getElementById('bizGrid');
                grid.innerHTML = '';
                let filtered = businesses;
                
                if(cat === 'favs') {
                    filtered = businesses.filter(b => this.favorites.includes(b.id));
                } else if(cat !== 'all') {
                    filtered = businesses.filter(b => b.category === cat);
                }

                filtered.forEach(b => {
                    const isFav = this.favorites.includes(b.id);
                    const card = document.createElement('div');
                    card.className = 'business-card';
                    card.innerHTML = `
                        <div class="card-header">
                            <h3 style="color:var(--deep-teal)">${b.name}</h3>
                            <span style="font-size:0.85rem; font-weight:700; color:var(--sunset-orange)">${b.category.toUpperCase()}</span>
                        </div>
                        <div class="card-body">
                            <p>📍 ${b.address}</p>
                            <p>📞 ${b.phone}</p>
                            <div style="background:var(--warm-cream); border-left:4px solid var(--golden); padding:10px; margin:15px 0; border-radius:4px; font-weight:bold; font-size:0.9rem;">
                                SPECIAL: ${b.deal}
                            </div>
                            <div style="display:flex; gap:10px;">
                                <button class="btn btn-primary" onclick="app.openModal(${b.id}, '${b.name}')">Review</button>
                                <button class="btn btn-outline" onclick="app.toggleFav(${b.id})">${isFav ? '💙' : '🤍'}</button>
                            </div>
                        </div>
                    `;
                    grid.appendChild(card);
                });
            },

            toggleFav: function(id) {
                if(this.favorites.includes(id)) {
                    this.favorites = this.favorites.filter(fid => fid !== id);
                } else { this.favorites.push(id); }
                document.getElementById('pFavs').innerText = this.favorites.length;
                this.render(document.querySelector('.nav-btn.active').innerText.includes('Favorites') ? 'favs' : 'all');
            },

            openModal: function(id, name) {
                this.activeBizId = id;
                document.getElementById('modalTitle').innerText = "Review " + name;
                document.getElementById('reviewModal').classList.add('active');
            },

            closeModal: function() {
                document.getElementById('reviewModal').classList.remove('active');
                document.getElementById('reviewText').value = '';
            },

            submitReview: function() {
                const text = document.getElementById('reviewText').value;
                if(!text) { alert("Please write a few words first!"); return; }
                this.reviews++;
                document.getElementById('pReviews').innerText = this.reviews;
                if(this.reviews === 1) document.getElementById('badgeStatus').innerText = "🏆 Badges: Local Reviewer";
                if(this.reviews === 5) document.getElementById('badgeStatus').innerText = "🏆 Badges: Community Leader";
                
                alert("Review Published! Your feedback helps the community.");
                this.closeModal();
            }
        };
    </script>
</body>
</html>