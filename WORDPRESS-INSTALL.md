# WordPress Theme Installation Guide

## Quick Start - Upload & Go Live! 🚀

Follow these simple steps to install your Long Beach Landscaping theme on WordPress:

---

## Step 1: Download the Theme ZIP

**File:** `longbeach-landscaping.zip` (27 KB)

This ZIP file is located in the root directory of this repository.

---

## Step 2: Install on WordPress

### Method A: Via WordPress Admin (Recommended)

1. **Log into your WordPress Admin Panel**
   - Go to: `https://yoursite.com/wp-admin`

2. **Navigate to Themes**
   - Click `Appearance` → `Themes`

3. **Add New Theme**
   - Click the `Add New` button at the top

4. **Upload Theme**
   - Click `Upload Theme` button
   - Click `Choose File`
   - Select `longbeach-landscaping.zip`
   - Click `Install Now`

5. **Activate**
   - Once uploaded, click `Activate`
   - Your theme is now live! 🎉

### Method B: Via FTP

1. **Extract the ZIP file**
   - Unzip `longbeach-landscaping.zip` on your computer
   - You'll get a folder called `longbeach-landscaping`

2. **Upload via FTP**
   - Connect to your server using FTP (FileZilla, Cyberduck, etc.)
   - Navigate to `/wp-content/themes/`
   - Upload the entire `longbeach-landscaping` folder

3. **Activate**
   - Go to WordPress Admin → `Appearance` → `Themes`
   - Find "Long Beach Landscaping" and click `Activate`

---

## Step 3: Configure Your Site (5 minutes)

### Set Homepage

1. Go to `Settings` → `Reading`
2. Select **"A static page"** for "Your homepage displays"
3. Click `Save Changes`

### Configure Permalinks

1. Go to `Settings` → `Permalinks`
2. Select **"Post name"** (recommended for SEO)
3. Click `Save Changes`
4. **Important:** This activates your custom post types!

### Customize Theme Settings

1. Go to `Appearance` → `Customize`
2. Configure:
   - **Hero Section**: Change title and subtitle
   - **Contact Information**: Add your address, phone, email
   - **Site Identity**: Upload your logo

---

## Step 4: Add Your Content

### Add Portfolio Items

1. In WordPress admin, look for **Portfolio** in the left menu
2. Click `Portfolio` → `Add New`
3. Fill in:
   - **Title**: Project name (e.g., "Modern Coastal Garden")
   - **Content**: Detailed project description
   - **Excerpt**: Location (e.g., "Belmont Shore Residence")
   - **Featured Image**: Upload project image (600x400px recommended)
   - **Portfolio Category**: Select or create category (Residential, Commercial, etc.)
4. Click `Publish`
5. **Repeat for 6-12 projects** for a complete gallery

### Add Services

1. Click `Services` → `Add New`
2. Fill in:
   - **Title**: Service name (e.g., "Landscape Design")
   - **Content**: Full service description
   - **Excerpt**: Short description for card display
3. Click `Publish`
4. **Add 6 services** (Design, Installation, Irrigation, Hardscape, Maintenance, Native Plants)

### Add Testimonials

1. Click `Testimonials` → `Add New`
2. Fill in:
   - **Title**: Client name (e.g., "Sarah Martinez")
   - **Content**: Full testimonial text
   - **Excerpt**: Location/title (e.g., "Belmont Shore")
3. Click `Publish`
4. **Add 3-5 testimonials**

---

## Step 5: Test Your Site

Visit your website homepage and you should see:

✅ Hero section with your custom text
✅ About section
✅ Services grid (default 6 services or your custom ones)
✅ Portfolio gallery (your projects with filtering)
✅ Testimonials slider
✅ Contact form
✅ Footer

---

## Troubleshooting

### Portfolio Items Not Showing?

**Fix:** Go to `Settings` → `Permalinks` and click "Save Changes" to flush rewrite rules.

### Menu Not Appearing?

**Fix:** Create a menu at `Appearance` → `Menus` and assign it to "Primary Menu" location.

### Contact Form Not Working?

**Fix:**
- Check your WordPress admin email at `Settings` → `General`
- Consider installing **WP Mail SMTP** plugin for better email delivery

### Images Not Displaying?

**Fix:** Make sure images are uploaded to WordPress Media Library, not referenced from external locations.

---

## What's Included in This Theme

### Template Files

- ✅ `index.php` - Main template
- ✅ `front-page.php` - Homepage template
- ✅ `single.php` - Single post template
- ✅ `page.php` - Page template
- ✅ `archive.php` - Archive template
- ✅ `search.php` - Search results template
- ✅ `404.php` - Error page template
- ✅ `header.php` - Header template
- ✅ `footer.php` - Footer template

### Functionality

- ✅ **Custom Post Types**: Portfolio, Services, Testimonials
- ✅ **Custom Taxonomies**: Portfolio Categories
- ✅ **AJAX Contact Form**: Built-in email functionality
- ✅ **Portfolio Filtering**: JavaScript-based category filtering
- ✅ **Testimonials Slider**: Auto-play carousel
- ✅ **Widget Areas**: 4 footer columns
- ✅ **Theme Customizer**: Hero section, contact info, logo
- ✅ **Responsive Design**: Mobile, tablet, desktop
- ✅ **SEO Optimized**: Clean semantic HTML5

---

## Recommended Plugins

Install these plugins for enhanced functionality:

### Essential (Highly Recommended)

1. **Yoast SEO** or **Rank Math**
   - SEO optimization and XML sitemaps
   - Install: `Plugins` → `Add New` → Search "Yoast SEO"

2. **WP Super Cache** or **WP Rocket**
   - Page caching for faster load times
   - Install: `Plugins` → `Add New` → Search "WP Super Cache"

3. **Wordfence Security**
   - Security scanning and firewall
   - Install: `Plugins` → `Add New` → Search "Wordfence"

### Optional Enhancements

4. **Contact Form 7** (if you want advanced form features)
5. **Smush** or **ShortPixel** (image optimization)
6. **UpdraftPlus** (automated backups)

---

## Next Steps After Installation

1. ✅ **Add Content** - Portfolio items, services, testimonials
2. ✅ **Upload Images** - High-quality project photos
3. ✅ **Customize Design** - Colors, logo, text
4. ✅ **Configure SEO** - Install Yoast SEO, add meta descriptions
5. ✅ **Enable SSL** - Ensure HTTPS is working
6. ✅ **Test Mobile** - Check responsiveness on phone/tablet
7. ✅ **Submit to Google** - Add site to Google Search Console
8. ✅ **Go Live!** 🎉

---

## Support & Documentation

- **Full Migration Guide**: See `MIGRATION-GUIDE.md` for detailed documentation
- **README**: See `README.md` for project overview
- **Theme Files**: Browse `wordpress-theme/longbeach-landscaping/` for source code

---

## File Structure

```
longbeach-landscaping.zip (27 KB)
└── longbeach-landscaping/
    ├── style.css           # Theme stylesheet (required)
    ├── functions.php       # Theme functions
    ├── header.php          # Header template
    ├── footer.php          # Footer template
    ├── front-page.php      # Homepage template
    ├── index.php           # Main template
    ├── single.php          # Single post
    ├── page.php            # Page template
    ├── archive.php         # Archive template
    ├── search.php          # Search results
    ├── 404.php             # Error page
    ├── readme.txt          # WordPress theme readme
    ├── screenshot.txt      # Screenshot placeholder
    └── js/
        └── script.js       # JavaScript functionality
```

---

## Technical Requirements

- **WordPress**: 5.8 or higher
- **PHP**: 7.4 or higher
- **MySQL**: 5.6+ or MariaDB 10.1+
- **HTTPS**: Recommended (free via Let's Encrypt)

---

## Going Live Checklist

Before launching your site publicly:

- [ ] All content added (portfolio, services, testimonials)
- [ ] Images optimized and uploaded
- [ ] Contact form tested
- [ ] Logo uploaded
- [ ] Contact information updated
- [ ] Social media links added
- [ ] SSL certificate installed (HTTPS)
- [ ] Google Analytics added (optional)
- [ ] Tested on mobile devices
- [ ] All links working
- [ ] SEO plugin installed and configured
- [ ] Backup system in place

---

## Success! 🎉

Your Long Beach Landscaping website is now ready to showcase your beautiful outdoor projects!

**Need help?** Review the comprehensive `MIGRATION-GUIDE.md` for detailed instructions on every aspect of the theme.

---

**Made with 🌱 for Long Beach Landscaping**

*Ready to transform outdoor spaces, one website at a time.*
