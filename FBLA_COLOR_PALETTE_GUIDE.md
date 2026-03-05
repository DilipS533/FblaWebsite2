# FBLA 2025–2026 Coding & Programming Event
## Color Palette & Design System Guide

---

## 1. PRIMARY PALETTE

### 1.1 FBLA Deep Blue
- **Hex Code:** `#003366` (or `#004080` for lighter variant)
- **RGB:** 0, 51, 102 (or 0, 64, 128)
- **Purpose:** Primary brand color, main backgrounds, headers, primary CTA buttons, navigation bars
- **Description:** Deep, authoritative blue reflecting FBLA's institutional trust and professional identity. Conveys stability, technology, and leadership.
- **Usage Tips:**
  - Use as background for hero sections and header/footer areas
  - Primary button background for high-priority actions
  - Text accents for important headings and section titles
  - Pairs well with white for maximum contrast

### 1.2 FBLA Bright Red
- **Hex Code:** `#E31E24`
- **RGB:** 227, 30, 36
- **Purpose:** Energy accent, secondary CTA buttons, hover states, alerts, and critical information
- **Description:** Vibrant, attention-grabbing red representing innovation, urgency, and FBLA's dynamic brand spirit. Used sparingly for maximum impact.
- **Usage Tips:**
  - Use for "Register," "Apply," or high-priority action buttons
  - Call-out badges for limited-time opportunities
  - Hover state for secondary buttons and links
  - Warning or important alerts (competitions closing, registration deadlines)
  - Accent striping or left borders on key cards/modules
  - **Caution:** Use conservatively to avoid visual overwhelm; limit to ~5% of design

### 1.3 Clean White
- **Hex Code:** `#FFFFFF`
- **RGB:** 255, 255, 255
- **Purpose:** Primary text background, card containers, text on dark backgrounds
- **Description:** Clean, neutral base providing contrast and readability. Essential for accessibility and modern aesthetic.
- **Usage Tips:**
  - All card and content containers
  - Text color on dark (blue, navy) backgrounds
  - Navigation backgrounds for clarity
  - Ensures 7:1+ contrast ratio with deep blue for accessibility

### 1.4 Off-White / Light Gray
- **Hex Code:** `#F5F7FA`
- **RGB:** 245, 247, 250
- **Purpose:** Secondary background, section separators, subtle backgrounds for alternating content areas
- **Description:** Soft, cool-toned white with slight blue tint. Creates visual breathing room without introducing new colors.
- **Usage Tips:**
  - Alternate background for every other section
  - Input field backgrounds
  - Code block or technical documentation backgrounds
  - Subtle visual hierarchy without contrast strain

---

## 2. SECONDARY & ACCENT COLORS

### 2.1 Tech Cyan / Accent Blue
- **Hex Code:** `#00A0D2`
- **RGB:** 0, 160, 210
- **Purpose:** Secondary accent, interactive elements, borders, feature highlights, link colors
- **Description:** Bright, approachable cyan representing innovation, technology, and forward-thinking. Complements deep blue while feeling modern and approachable.
- **Usage Tips:**
  - Secondary button backgrounds
  - Active states for form inputs and checkboxes
  - Link hover effects
  - Accent borders on featured cards or sections
  - Icon colors for primary navigation
  - Progress bars and loading indicators

### 2.2 Neutral Dark Gray
- **Hex Code:** `#333333`
- **RGB:** 51, 51, 51
- **Purpose:** Primary text color, secondary headings, body copy
- **Description:** Dark gray (not pure black) providing excellent readability while being easier on the eyes in extended reading. Softer than pure black.
- **Usage Tips:**
  - All body paragraph text
  - Secondary headings and subheadings
  - Menu text and navigation labels
  - Form labels and descriptive text

### 2.3 Medium Gray
- **Hex Code:** `#666666`
- **RGB:** 102, 102, 102
- **Purpose:** Secondary text, disabled states, metadata, footer text, captions
- **Description:** Mid-tone gray for de-emphasized content. Less prominent than primary text but still accessible.
- **Usage Tips:**
  - Metadata, timestamps, and supporting information
  - Disabled button text and form inputs
  - Footer secondary information
  - Placeholder text in form fields
  - Image captions and figure descriptions

### 2.4 Light Gray / Border Color
- **Hex Code:** `#CCCCCC` or `#E0E0E0`
- **RGB:** 204, 204, 204 (or 224, 224, 224)
- **Purpose:** Borders, dividers, subtle visual separation, input field borders
- **Description:** Very light gray for minimal visual weight. Separates elements without heavy visual contrast.
- **Usage Tips:**
  - Card borders and dividing lines
  - Input field borders (non-focused state)
  - Subtle horizontal dividers between sections
  - Button borders for secondary/tertiary buttons

### 2.5 Success Green
- **Hex Code:** `#28A745`
- **RGB:** 40, 167, 69
- **Purpose:** Success messages, confirmation states, completed actions, positive feedback
- **Description:** Warm, accessible green signaling completion, approval, or successful outcomes. Independent of red/green colorblindness issues due to brightness.
- **Usage Tips:**
  - Success alerts and confirmation messages
  - Completed badges or checkmarks
  - Form validation success indicators
  - Progress completion states

### 2.6 Warning Orange
- **Hex Code:** `#FFC107`
- **RGB:** 255, 193, 7
- **Purpose:** Warnings, pending states, caution messages, important notices
- **Description:** Bright, warm orange conveying attention without severity. Distinguishable from both red (danger) and green (success).
- **Usage Tips:**
  - Pending or processing states
  - Caution notices (e.g., "Verify your information")
  - In-progress badges
  - Important but non-critical alerts

### 2.7 Danger Red (Error State)
- **Hex Code:** `#DC3545`
- **RGB:** 220, 53, 69
- **Purpose:** Error messages, validation errors, critical alerts, destructive actions
- **Description:** Softer red than the FBLA accent red, specific to error and danger states. Distinguishes from general emphasis.
- **Usage Tips:**
  - Form validation errors
  - Error message text and backgrounds
  - Destructive action confirmations (delete, remove)
  - Critical alert borders

---

## 3. USAGE GUIDELINES

### 3.1 Backgrounds & Text Contrast

#### Primary Backgrounds
- **Dark Blue (#003366) + White (#FFFFFF) text**
  - Contrast Ratio: 15.7:1 ✓ WCAG AAA (Exceeds accessibility requirements)
  - **Use for:** Hero sections, headers, footers, primary CTAs

- **Off-White (#F5F7FA) + Dark Gray (#333333) text**
  - Contrast Ratio: 12.5:1 ✓ WCAG AAA
  - **Use for:** Body content sections, secondary backgrounds

- **White (#FFFFFF) + Dark Gray (#333333) text**
  - Contrast Ratio: 13:1 ✓ WCAG AAA
  - **Use for:** Card containers, content modules

#### Secondary Backgrounds (Caution Required)
- **Do NOT use** Bright Red (#E31E24) as a full background for extended text
- **Do NOT use** Cyan (#00A0D2) as primary background; use sparingly or with white overlay
- These colors work best as accents, borders, or small UI elements

### 3.2 Buttons & Interactive Elements

#### Primary Button (High Priority Actions)
```
Background: #003366 (FBLA Deep Blue)
Text: #FFFFFF (White)
Border: None
Hover: #004080 (Lighter blue) with 1–2px downward shadow
Active: #002244 (Darker blue)
```

#### Secondary Button (Moderate Priority)
```
Background: #FFFFFF (White)
Text: #003366 (FBLA Deep Blue)
Border: 2px solid #003366
Hover: Background changes to #F5F7FA with #E31E24 border (FBLA Red)
Active: Background darkens slightly
```

#### Accent / CTA Button (Register, Apply, Special Actions)
```
Background: #E31E24 (FBLA Bright Red)
Text: #FFFFFF (White)
Border: None
Hover: #B71620 (Darker red) with elevated shadow
Active: #8B0F15 (Darkest red)
```

#### Tertiary / Ghost Button
```
Background: Transparent
Text: #00A0D2 (Cyan Accent)
Border: 1px solid #00A0D2
Hover: Background becomes #F5F7FA, Text remains #00A0D2
Active: Text becomes #003366, Border becomes #003366
```

#### Disabled State (All Buttons)
```
Background: #E0E0E0 (Light Gray)
Text: #999999 (Medium Gray)
Cursor: not-allowed
Opacity: 0.6
```

### 3.3 Headers, Footers & Navigation

#### Header/Navigation Bar
- **Background:** #003366 (FBLA Deep Blue)
- **Text:** #FFFFFF (White)
- **Active Link:** #00A0D2 (Cyan) with 2px bottom border
- **Hover Link:** #F5F7FA (Off-White) text with slight background highlight
- **Logo:** White or color-variant approved by FBLA branding
- **Search Input:** White background with light gray border, dark gray text

#### Footer
- **Background:** #003366 (FBLA Deep Blue)
- **Primary Text:** #FFFFFF (White)
- **Secondary Text:** #B3D9FF (Light Blue, 70% opacity white)
- **Links:** #00A0D2 (Cyan) with underline on hover
- **Dividers:** #004080 (Lighter blue)
- **Social Icons:** White or cyan

### 3.4 Cards & Content Modules

#### Standard Card Container
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #E0E0E0 (Light Gray) or 1px solid #CCCCCC
- **Shadow:** Subtle (0 2px 8px rgba(0, 51, 102, 0.1))
- **Corner Radius:** 6–8px (consistent roundness)
- **Hover State:** Slight lift with shadow increase (0 4px 12px rgba(0, 51, 102, 0.15))

#### Highlighted / Featured Card
- **Background:** #FFFFFF (White)
- **Border:** 3px solid #E31E24 (FBLA Red) or 2px solid #00A0D2 (Cyan)
- **Accent Bar:** 4px top border in #E31E24 (Red)

#### Event/Opportunity Card
- **Header Section:** #F5F7FA (Off-White) or #00A0D2 (Cyan with white text)
- **Body Section:** #FFFFFF (White)
- **Status Badge:** Green (#28A745), Orange (#FFC107), or Red (#DC3545)

### 3.5 Forms & Inputs

#### Input Field (Default)
- **Background:** #FFFFFF (White)
- **Border:** 1px solid #CCCCCC (Light Gray)
- **Text:** #333333 (Dark Gray)
- **Placeholder:** #999999 (Medium Gray, 60% opacity)

#### Input Field (Focus)
- **Border:** 2px solid #00A0D2 (Cyan Accent)
- **Box Shadow:** 0 0 0 3px rgba(0, 160, 210, 0.1)
- **Background:** Remains white

#### Input Field (Error)
- **Border:** 2px solid #DC3545 (Error Red)
- **Background:** #FFF5F5 (very light red)
- **Error Text Below:** #DC3545 in small font

#### Labels
- **Text:** #333333 (Dark Gray)
- **Font Weight:** 500–600
- **Required Asterisk:** #E31E24 (Red)

### 3.6 Badges & Status Indicators

| Status | Color | Use Case |
|--------|-------|----------|
| **Active/Success** | #28A745 (Green) | Registration open, accepted, approved |
| **In Progress** | #FFC107 (Orange) | Processing, pending decision |
| **Warning/Urgent** | #E31E24 (Red) | Closing soon, limited spots, requires action |
| **Inactive** | #999999 (Medium Gray) | Registration closed, event ended, not available |
| **Featured** | #00A0D2 (Cyan) | Recommended, highlighted opportunity |

### 3.7 Accessibility & Readability

#### Color Contrast Standards
All text must meet **WCAG AA standards (4.5:1 contrast ratio)** at minimum:

**Compliant Combinations:**
- ✓ Dark Blue (#003366) + White (#FFFFFF): 15.7:1
- ✓ Dark Blue (#003366) + Off-White (#F5F7FA): 11.2:1
- ✓ Dark Gray (#333333) + White (#FFFFFF): 13:1
- ✓ Dark Gray (#333333) + Off-White (#F5F7FA): 11.8:1
- ✓ Medium Gray (#666666) + White (#FFFFFF): 7.3:1
- ✓ Cyan (#00A0D2) + White (#FFFFFF): 6.5:1
- ✓ Green (#28A745) + White (#FFFFFF): 7.2:1
- ✓ Orange (#FFC107) + Dark Gray (#333333): 5.2:1 (AA compliant)

**Non-Compliant (Avoid):**
- ✗ Cyan (#00A0D2) + Off-White (#F5F7FA): 3.8:1 (use only for non-essential decorative text)
- ✗ Light Gray text on White: Less than 4.5:1 (use only for placeholders/captions)

#### Color Blindness Considerations
- **Avoid red-green combinations for critical information** (e.g., don't use only red and green for status without other indicators)
- **Use text, icons, or patterns in addition to color** for differentiation
- **Test with tools:** Use WebAIM Contrast Checker, Color Oracle, or similar tools to validate

#### Text Legibility Best Practices
- **Body Text:** Use #333333 (Dark Gray) on white or off-white backgrounds
- **Minimum Font Size:** 14px for body content, 12px for secondary information
- **Line Height:** 1.5–1.6 for comfortable reading
- **Maximum Line Length:** 65–75 characters per line to prevent eye strain
- **Font Weight:** Regular (400) for body, 500–600 for labels, 700 for headings

---

## 4. GRADIENT & ACCENT EFFECTS (Optional Tech Enhancement)

These optional effects add visual interest while maintaining professionalism. Use conservatively.

### 4.1 Subtle Gradient Overlay
```css
background: linear-gradient(135deg, #003366 0%, #004080 100%);
/* Adds depth to large sections without feeling overdone */
```
**Where to Use:**
- Hero section backgrounds
- CTA button hover states
- Featured section backgrounds
- Header behind text

### 4.2 Accent Line / Underline (Modern Touch)
```css
border-top: 3px solid #00A0D2;
/* or */
border-left: 4px solid #E31E24;
```
**Where to Use:**
- Top of featured cards
- Left side of testimonials or quotes
- Above section headers
- Button underlines on hover

### 4.3 Diagonal Stripe Pattern (Optional)
```
Use thin diagonal stripes in #F5F7FA over white or light backgrounds
Effect: Adds texture without overwhelming the design
Applications: Background of FAQ sections, team profiles, or data showcase areas
```

### 4.4 Glow Effect on Focus (Accessibility + Visual Feedback)
```css
box-shadow: 0 0 0 3px rgba(0, 160, 210, 0.2);
/* Creates soft glow around focused/active elements */
```
**Where to Use:**
- Form inputs on focus
- Buttons on hover/active
- Highlighted navigation items

### 4.5 Glassmorphism Cards (Modern, Optional)
```css
background: rgba(255, 255, 255, 0.95);
backdrop-filter: blur(10px);
border: 1px solid rgba(255, 255, 255, 0.3);
```
**Where to Use:**
- Overlay modals or lightboxes
- Featured spotlight cards
- Testimonial cards
**Caution:** Use sparingly; ensure text remains readable

---

## 5. PRACTICAL IMPLEMENTATION GUIDE

### 5.1 CSS Custom Properties (Recommended)
```css
:root {
  /* Primary Colors */
  --primary-blue: #003366;
  --primary-blue-light: #004080;
  --primary-blue-dark: #002244;
  --accent-red: #E31E24;
  --accent-red-hover: #B71620;
  --accent-cyan: #00A0D2;

  /* Neutral Colors */
  --white: #FFFFFF;
  --off-white: #F5F7FA;
  --dark-gray: #333333;
  --medium-gray: #666666;
  --light-gray: #CCCCCC;
  --border-gray: #E0E0E0;

  /* Semantic Colors */
  --success: #28A745;
  --warning: #FFC107;
  --error: #DC3545;

  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0, 51, 102, 0.08);
  --shadow-md: 0 2px 8px rgba(0, 51, 102, 0.1);
  --shadow-lg: 0 4px 12px rgba(0, 51, 102, 0.15);
}
```

### 5.2 Button Usage Examples

**Primary CTA (Register, Apply, Submit)**
```css
.btn-primary {
  background: linear-gradient(135deg, #003366 0%, #004080 100%);
  color: white;
  border: none;
  padding: 12px 28px;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #004080 0%, #005099 100%);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
```

**Secondary Button (Learn More, View Details)**
```css
.btn-secondary {
  background: white;
  color: #003366;
  border: 2px solid #003366;
  padding: 10px 26px;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background: #003366;
  color: white;
  box-shadow: var(--shadow-md);
}
```

**Accent Button (Limited-Time Actions)**
```css
.btn-accent {
  background: #E31E24;
  color: white;
  border: none;
  padding: 12px 28px;
  font-weight: 700;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(227, 30, 36, 0.3);
}

.btn-accent:hover {
  background: #B71620;
  box-shadow: 0 6px 16px rgba(227, 30, 36, 0.4);
  transform: translateY(-2px);
}
```

### 5.3 Card Layout Example

```css
.card {
  background: white;
  border: 1px solid #E0E0E0;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card.featured {
  border-top: 4px solid #E31E24;
  box-shadow: 0 4px 16px rgba(0, 51, 102, 0.12);
}

.card-header {
  color: #003366;
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
}

.card-body {
  color: #333333;
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.card-footer {
  border-top: 1px solid #E0E0E0;
  padding-top: 1rem;
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}
```

### 5.4 Form Example

```css
.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  color: #333333;
  font-weight: 600;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.form-label .required {
  color: #E31E24;
  margin-left: 3px;
}

.form-input,
.form-select,
.form-textarea {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #CCCCCC;
  border-radius: 6px;
  font-size: 1rem;
  font-family: inherit;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background: white;
  color: #333333;
}

.form-input::placeholder,
.form-textarea::placeholder {
  color: #999999;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: #00A0D2;
  box-shadow: 0 0 0 3px rgba(0, 160, 210, 0.1);
  background: white;
}

.form-error {
  color: #DC3545;
  font-size: 0.875rem;
  margin-top: 0.5rem;
}

.form-input.error {
  border-color: #DC3545;
  background: #FFF5F5;
}

.form-input.success {
  border-color: #28A745;
  background: #F0FFF4;
}
```

---

## 6. ACCESSIBILITY CHECKLIST

- [ ] All text meets WCAG AA contrast ratio (4.5:1) minimum
- [ ] Color is not the only method to convey information (use icons, text, patterns)
- [ ] Form labels are associated with inputs (use `<label for="id">`)
- [ ] Focus states are clearly visible (at least 2px outline or shadow)
- [ ] Interactive elements have sufficient size (minimum 44x44px for touch targets)
- [ ] Color blindness tested (use tools like Color Oracle or Blind Specific)
- [ ] Hover and active states are distinct and accessible
- [ ] Disabled state is visually clear without relying on color alone
- [ ] Error messages are displayed with both color and text

---

## 7. QUICK REFERENCE COLOR PALETTE TABLE

| Element | Background | Text | Border/Accent |
|---------|-----------|------|----------------|
| Header/Footer | #003366 | #FFFFFF | — |
| Primary Button | #003366 | #FFFFFF | — |
| Secondary Button | #FFFFFF | #003366 | #003366 |
| Accent Button | #E31E24 | #FFFFFF | — |
| Card Container | #FFFFFF | #333333 | #E0E0E0 |
| Featured Card | #FFFFFF | #333333 | #E31E24 (top) |
| Input Field | #FFFFFF | #333333 | #CCCCCC |
| Section Background | #F5F7FA | #333333 | — |
| Success Badge | #28A745 | #FFFFFF | — |
| Warning Badge | #FFC107 | #333333 | — |
| Error Badge | #DC3545 | #FFFFFF | — |
| Link (default) | — | #00A0D2 | — |
| Link (hover) | #F5F7FA | #003366 | #00A0D2 (underline) |

---

## 8. DESIGN PRINCIPLES SUMMARY

1. **Authority & Trust:** Deep blue primary color conveys professionalism suitable for a national student competition.
2. **Energy & Innovation:** Red and cyan accents add modern, tech-forward feel without overwhelming.
3. **Clean & Accessible:** Ample white space, high contrast ratios, and semantic color usage ensure readability and inclusivity.
4. **Consistent & Scalable:** CSS custom properties and defined usage rules make implementation consistent across all pages.
5. **FBLA Aligned:** Reflects official FBLA branding while maintaining modern design standards.

---

## 9. FINAL NOTES

- **Consistency is Key:** Use this palette uniformly across all pages and features.
- **Test with Real Users:** Conduct accessibility testing with users of varying abilities and color vision.
- **Responsive Design:** Ensure color and contrast requirements are maintained on all screen sizes.
- **Dark Mode (Optional Future Enhancement):** If dark mode is desired, invert the primary colors and adjust contrast accordingly.
- **FBLA Brand Compliance:** Always verify any chosen design against official FBLA brand guidelines to ensure alignment.

---

**Design Guide Version:** 1.0  
**Last Updated:** March 4, 2026  
**Created for:** FBLA 2025–2026 Coding & Programming Competitive Event
