# Long Beach Landscaping - WordPress Migration Guide

This guide will help you migrate the Long Beach Landscaping portfolio website to WordPress.org.

## Table of Contents

1. [Project Overview](#project-overview)
2. [What's Included](#whats-included)
3. [WordPress Theme Installation](#wordpress-theme-installation)
4. [Setting Up Your Content](#setting-up-your-content)
5. [Customization](#customization)
6. [Adding Content](#adding-content)
7. [Forms & Contact](#forms--contact)
8. [Going Live](#going-live)

---

## Project Overview

The Long Beach Landscaping website is a professional portfolio website designed for landscaping businesses in Long Beach, California. It features:

- Modern, responsive design
- Portfolio gallery with filtering
- Services showcase
- Testimonials slider
- Contact form with AJAX submission
- SEO-friendly structure
- Fast loading times
- Mobile-first approach

---

## What's Included

### Static Website Files (Root Directory)

- `index.html` - Static HTML version of the website
- `styles.css` - Main stylesheet
- `script.js` - JavaScript functionality
- `images/` - Directory for images

### WordPress Theme Files (`wordpress-theme/longbeach-landscaping/`)

Complete WordPress theme ready to install:

- `style.css` - Theme stylesheet with WordPress header
- `functions.php` - Theme functionality and custom post types
- `header.php` - Site header template
- `footer.php` - Site footer template
- `front-page.php` - Homepage template
- `index.php` - Main template file
- `js/script.js` - WordPress-compatible JavaScript

---

## WordPress Theme Installation

### Prerequisites

1. A WordPress installation (5.8 or higher)
2. PHP 7.4 or higher
3. MySQL 5.6 or higher (or MariaDB 10.1+)
4. FTP access or WordPress admin access

### Installation Steps

#### Method 1: Via WordPress Admin (Recommended)

1. **Prepare the Theme**
   ```bash
   cd wordpress-theme
   zip -r longbeach-landscaping.zip longbeach-landscaping/
   ```

2. **Upload to WordPress**
   - Log into your WordPress admin panel
   - Navigate to `Appearance > Themes > Add New`
   - Click `Upload Theme`
   - Choose the `longbeach-landscaping.zip` file
   - Click `Install Now`
   - After installation, click `Activate`

#### Method 2: Via FTP

1. **Connect to Your Server**
   - Use an FTP client (FileZilla, Cyberduck, etc.)
   - Connect to your WordPress hosting

2. **Upload Theme Files**
   - Navigate to `/wp-content/themes/`
   - Upload the entire `longbeach-landscaping` folder
   - Go to WordPress admin `Appearance > Themes`
   - Find and activate "Long Beach Landscaping"

---

## Setting Up Your Content

### 1. Configure Site Settings

**Basic Settings** (`Settings > General`):
- Site Title: "Long Beach Landscaping"
- Tagline: "Premium Outdoor Design"
- WordPress Address & Site Address: Your domain URL

**Permalink Settings** (`Settings > Permalinks`):
- Select "Post name" for SEO-friendly URLs
- Save changes

### 2. Set Homepage

1. Go to `Settings > Reading`
2. Select "A static page" for homepage displays
3. Choose your homepage from the dropdown
4. Save changes

### 3. Create Menus

**Primary Menu** (`Appearance > Menus`):
1. Create a new menu called "Primary Menu"
2. Add custom links:
   - Home: `#home`
   - About: `#about`
   - Services: `#services`
   - Portfolio: `#portfolio`
   - Testimonials: `#testimonials`
   - Contact: `#contact`
3. Assign to "Primary Menu" location
4. Save menu

**Footer Menu** (optional):
1. Create a new menu called "Footer Menu"
2. Add links to important pages
3. Assign to "Footer Menu" location

---

## Customization

### Theme Customizer

Access via `Appearance > Customize`:

#### Hero Section
- **Hero Title**: Main headline on homepage
- **Hero Subtitle**: Subheadline text

#### Contact Information
- **Address**: Your business address
- **Phone Number**: Contact phone
- **Email**: Contact email

#### Logo
- Upload your logo via `Site Identity > Logo`
- Recommended size: 400x100px

#### Colors (optional)
- Use `Colors` section to customize theme colors
- Or edit CSS variables in `style.css`

---

## Adding Content

### Portfolio Items

1. Go to `Portfolio > Add New` in WordPress admin
2. Add project details:
   - **Title**: Project name (e.g., "Modern Coastal Garden")
   - **Content**: Detailed project description
   - **Excerpt**: Short description for gallery (e.g., "Belmont Shore Residence")
   - **Featured Image**: Main project image (600x400px recommended)
3. Assign **Portfolio Category**:
   - Create categories: Residential, Commercial, Hardscape, Maintenance
4. Publish

**Adding Multiple Projects:**
- Add 6-12 portfolio items for a complete gallery
- Use high-quality images (compressed for web)
- Write compelling descriptions

### Services

1. Go to `Services > Add New`
2. Add service details:
   - **Title**: Service name (e.g., "Landscape Design")
   - **Content**: Full service description
   - **Excerpt**: Short description for cards
   - **Featured Image**: Service icon or image (optional)
3. Publish

**Default Services to Add:**
- Landscape Design
- Installation
- Irrigation Systems
- Hardscaping
- Maintenance
- Native Plants

### Testimonials

1. Go to `Testimonials > Add New`
2. Add testimonial:
   - **Title**: Client name (e.g., "Sarah Martinez")
   - **Content**: Testimonial text (testimonial body)
   - **Excerpt**: Location/title (e.g., "Belmont Shore")
3. Publish

**Tips:**
- Add 3-5 testimonials minimum
- Keep testimonials authentic and specific
- Include client location for local credibility

### Pages

#### Create About Page
1. Go to `Pages > Add New`
2. Title: "About"
3. Add your company history and story
4. Add a featured image (team photo, office, etc.)
5. Publish

**The front-page.php template will automatically pull content from this page.**

---

## Forms & Contact

### Contact Form

The theme includes a built-in AJAX contact form that:
- Sends emails to the WordPress admin email
- Validates user input
- Shows success/error messages
- Works without page reload

**To Configure:**

1. **Set Admin Email** (`Settings > General`):
   - Update "Email Address" to receive form submissions

2. **Test the Form:**
   - Submit a test message from your contact section
   - Check your email for the submission

### Alternative: Use Contact Form 7

For advanced form features:

1. Install Contact Form 7 plugin
2. Create a new form
3. Edit `front-page.php` contact section
4. Replace form HTML with Contact Form 7 shortcode:
   ```php
   <?php echo do_shortcode('[contact-form-7 id="123"]'); ?>
   ```

---

## Images & Media

### Image Sizes

The theme registers these image sizes:
- **Portfolio**: 600x400px
- **About**: 800x600px
- **Thumbnail**: 150x150px

### Optimizing Images

Before uploading:
1. Resize images to recommended dimensions
2. Compress using tools like:
   - TinyPNG (https://tinypng.com)
   - ImageOptim (Mac)
   - Squoosh (https://squoosh.app)
3. Target: Under 200KB per image

### Adding Images

1. Go to `Media > Add New`
2. Upload images
3. Add descriptive alt text for SEO
4. Use in posts, pages, and portfolio items

---

## Widgets (Footer)

### Configure Footer Widgets

Go to `Appearance > Widgets`:

**Footer Column 1:**
- Add "Text" widget
- Title: "Long Beach Landscaping"
- Content: Company description

**Footer Column 2:**
- Add "Navigation Menu" widget
- Select your footer menu

**Footer Column 3:**
- Add "Text" widget with services list

**Footer Column 4:**
- Add "Text" widget with service areas

---

## Plugins Recommended

### Essential Plugins

1. **Yoast SEO** or **Rank Math**
   - SEO optimization
   - XML sitemaps
   - Meta descriptions

2. **WP Super Cache** or **WP Rocket**
   - Page caching
   - Speed optimization

3. **Wordfence Security**
   - Security scanning
   - Firewall protection

4. **UpdraftPlus**
   - Automatic backups
   - Easy restoration

5. **Contact Form 7** (optional)
   - Advanced form features
   - Spam protection with reCAPTCHA

### Optional Enhancements

1. **Instagram Feed**
   - Display your Instagram photos
   - Great for showcasing recent work

2. **Google Analytics**
   - Track website visitors
   - Understand user behavior

---

## Going Live

### Pre-Launch Checklist

- [ ] All content added (portfolio, services, testimonials)
- [ ] Images optimized and uploaded
- [ ] Contact form tested and working
- [ ] Menus configured
- [ ] Logo uploaded
- [ ] Contact information updated
- [ ] Social media links added
- [ ] SSL certificate installed (HTTPS)
- [ ] Google Analytics added
- [ ] Site tested on mobile devices
- [ ] All links working
- [ ] 404 page checked

### Performance Optimization

1. **Enable Caching**
   - Install WP Super Cache or similar
   - Configure caching settings

2. **Optimize Database**
   - Use WP-Optimize plugin
   - Clean up post revisions

3. **CDN Setup** (optional)
   - Cloudflare (free tier available)
   - StackPath
   - BunnyCDN

4. **Image Optimization**
   - Install Smush or ShortPixel
   - Compress existing images
   - Enable lazy loading

### SEO Setup

1. **Install SEO Plugin**
   - Yoast SEO or Rank Math

2. **Configure SEO Settings**
   - Add meta descriptions
   - Optimize page titles
   - Submit XML sitemap to Google Search Console

3. **Google My Business**
   - Create/claim your listing
   - Add accurate business information
   - Get reviews from satisfied customers

4. **Local SEO**
   - Include "Long Beach" in key pages
   - Add location pages if serving multiple areas
   - Create local business schema markup

---

## Customization Tips

### Changing Colors

Edit `style.css` CSS variables (lines 1-20):

```css
:root {
    --primary-color: #2d5016;      /* Main green */
    --primary-light: #3d6b1f;      /* Lighter green */
    --secondary-color: #7c9a5e;    /* Accent green */
    --accent-color: #c4a569;       /* Gold accent */
}
```

### Adding Custom CSS

1. Go to `Appearance > Customize > Additional CSS`
2. Add your custom styles
3. Preview and save

### Child Theme (Advanced)

For major customizations, create a child theme:

1. Create folder: `wp-content/themes/longbeach-child/`
2. Create `style.css`:
   ```css
   /*
   Theme Name: Long Beach Landscaping Child
   Template: longbeach-landscaping
   */
   ```
3. Create `functions.php`:
   ```php
   <?php
   add_action('wp_enqueue_scripts', 'child_theme_styles');
   function child_theme_styles() {
       wp_enqueue_style('parent-style', get_template_directory_uri() . '/style.css');
   }
   ```
4. Activate child theme

---

## Troubleshooting

### Common Issues

**Issue: Portfolio/Services not showing**
- Solution: Go to `Settings > Permalinks` and click "Save Changes" to flush rewrite rules

**Issue: Images not displaying**
- Solution: Check file paths, ensure images are uploaded to WordPress media library

**Issue: Contact form not sending**
- Solution: Check WordPress email settings, consider SMTP plugin (WP Mail SMTP)

**Issue: Menu not displaying**
- Solution: Create menu and assign to "Primary Menu" location in `Appearance > Menus`

**Issue: Theme looks broken**
- Solution: Clear cache (browser and WordPress cache plugins)

---

## Support & Resources

### WordPress Resources

- **WordPress Codex**: https://codex.wordpress.org/
- **WordPress Support**: https://wordpress.org/support/
- **WordPress TV**: https://wordpress.tv/ (tutorials)

### Theme Support

For theme-specific questions:
1. Check this migration guide
2. Review theme files (especially functions.php)
3. WordPress community forums
4. Hire a WordPress developer if needed

### Recommended Reading

- WordPress theme development
- SEO best practices
- Website security
- Performance optimization

---

## Maintenance

### Regular Tasks

**Daily:**
- Check for spam comments
- Monitor contact form submissions

**Weekly:**
- Update plugins and themes
- Check website functionality
- Review analytics

**Monthly:**
- Update WordPress core
- Review security scans
- Backup website
- Check broken links
- Review SEO performance

---

## Conclusion

Your Long Beach Landscaping website is now ready for WordPress! This migration provides:

✅ Full CMS control over content
✅ Easy portfolio management
✅ Client testimonials system
✅ Built-in contact form
✅ Mobile-responsive design
✅ SEO-friendly structure
✅ Fast performance
✅ Scalability for growth

**Next Steps:**
1. Add your content (portfolio, services, testimonials)
2. Customize design (colors, logo, images)
3. Configure SEO settings
4. Test thoroughly
5. Launch your site!

Good luck with your new website! 🌱🏡
