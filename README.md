# Long Beach Landscaping Portfolio Website

A professional, modern portfolio website for landscaping businesses in Long Beach, California.

![Long Beach Landscaping](https://img.shields.io/badge/Status-Ready-brightgreen)
![WordPress](https://img.shields.io/badge/WordPress-Compatible-blue)
![License](https://img.shields.io/badge/License-GPL--2.0-lightgrey)

## Overview

This repository contains a complete landscaping portfolio website with both **static HTML** and **WordPress theme** versions. Perfect for landscaping, lawn care, and outdoor design businesses looking to showcase their work and attract new clients.

## Features

✨ **Modern Design**
- Professional, clean layout
- Green color scheme perfect for landscaping
- Fully responsive (mobile, tablet, desktop)
- Smooth animations and transitions

🎨 **Portfolio Gallery**
- Filterable project gallery
- Category-based filtering
- Hover effects with project details
- Optimized image display

💼 **Business Sections**
- Hero section with call-to-action
- About us section
- Services showcase (6 service cards)
- Portfolio gallery
- Client testimonials slider
- Contact form with validation
- Footer with business info

📱 **Mobile-First**
- Responsive navigation
- Touch-friendly interface
- Optimized for all screen sizes

⚡ **Performance**
- Fast loading times
- Optimized CSS and JavaScript
- Lazy loading for images
- Minimal dependencies

## Repository Structure

```
.
├── index.html                    # Static HTML website
├── styles.css                    # Main stylesheet
├── script.js                     # JavaScript functionality
├── images/                       # Images directory
│   └── README.md                # Image guidelines
├── wordpress-theme/              # WordPress theme
│   └── longbeach-landscaping/   # Theme directory
│       ├── style.css            # Theme stylesheet
│       ├── functions.php        # Theme functions
│       ├── header.php           # Header template
│       ├── footer.php           # Footer template
│       ├── front-page.php       # Homepage template
│       ├── index.php            # Main template
│       └── js/
│           └── script.js        # WordPress JavaScript
├── MIGRATION-GUIDE.md           # Complete WordPress migration guide
└── README.md                    # This file
```

## Quick Start

### Static Website (HTML)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/longbeach-landscaping.git
   cd longbeach-landscaping
   ```

2. **Add your images**
   - Place your images in the `images/` directory
   - Follow naming conventions in `images/README.md`

3. **Customize content**
   - Edit `index.html` to update text, business info
   - Modify `styles.css` for colors and styling
   - Update contact information

4. **Deploy**
   - Upload files to your web hosting
   - Or use services like Netlify, Vercel, or GitHub Pages

### WordPress Theme

1. **Prepare the theme**
   ```bash
   cd wordpress-theme
   zip -r longbeach-landscaping.zip longbeach-landscaping/
   ```

2. **Install in WordPress**
   - Go to `Appearance > Themes > Add New > Upload Theme`
   - Upload the ZIP file
   - Activate the theme

3. **Configure**
   - Follow the comprehensive [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md)
   - Add your content (portfolio, services, testimonials)
   - Customize via WordPress Customizer

## Customization

### Changing Colors

Edit CSS variables in `styles.css` (or WordPress `style.css`):

```css
:root {
    --primary-color: #2d5016;      /* Main green */
    --primary-light: #3d6b1f;      /* Lighter green */
    --secondary-color: #7c9a5e;    /* Accent green */
    --accent-color: #c4a569;       /* Gold accent */
}
```

### Business Information

Update contact details in:
- **HTML**: Edit `index.html` contact section
- **WordPress**: Use Customizer (`Appearance > Customize > Contact Information`)

### Adding Content

#### Static Version:
- Edit HTML directly in `index.html`

#### WordPress Version:
- Portfolio: `Portfolio > Add New`
- Services: `Services > Add New`
- Testimonials: `Testimonials > Add New`
- See [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md) for details

## WordPress Features

The WordPress theme includes:

- **Custom Post Types**
  - Portfolio items
  - Services
  - Testimonials

- **Custom Taxonomies**
  - Portfolio categories

- **Theme Customizer Settings**
  - Hero section text
  - Contact information
  - Logo upload
  - Custom colors

- **Widget Areas**
  - 4 footer columns

- **Built-in Features**
  - AJAX contact form
  - Portfolio filtering
  - Testimonials slider
  - Mobile menu
  - Smooth scrolling
  - Back to top button

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Requirements

### Static Website
- Any web server
- No special requirements

### WordPress Theme
- WordPress 5.8+
- PHP 7.4+
- MySQL 5.6+ or MariaDB 10.1+

## Documentation

- **[MIGRATION-GUIDE.md](MIGRATION-GUIDE.md)** - Complete guide for WordPress migration
- **[images/README.md](images/README.md)** - Image guidelines and specifications

## License

This theme is licensed under the GPL v2 or later.

## Credits

- **Design & Development**: Long Beach Landscaping Theme
- **Fonts**: Google Fonts (Montserrat, Open Sans)
- **Icons**: Emoji icons (universal support)

## Support

For support and questions:
1. Read the [MIGRATION-GUIDE.md](MIGRATION-GUIDE.md)
2. Check WordPress.org support forums
3. Review theme files and comments

## Changelog

### Version 1.0.0 (2024)
- Initial release
- Static HTML website
- WordPress theme
- Full documentation
- Portfolio, services, and testimonials features
- Contact form with AJAX
- Responsive design
- SEO optimization

## Screenshots

### Homepage Hero Section
Modern hero section with call-to-action buttons and smooth animations.

### Portfolio Gallery
Filterable portfolio gallery showcasing your best landscaping projects.

### Services Section
Six service cards highlighting your landscaping offerings.

### Testimonials
Sliding testimonials from satisfied clients.

### Contact Form
Working contact form with validation and AJAX submission.

## Future Enhancements

Planned features:
- [ ] Blog section template
- [ ] Additional page templates
- [ ] Instagram feed integration
- [ ] Google Maps integration
- [ ] Before/After image slider
- [ ] Booking/scheduling system
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## About

This website template was created specifically for landscaping businesses in Long Beach, California, but can be easily adapted for landscaping companies anywhere. The design focuses on showcasing beautiful outdoor spaces while maintaining fast load times and excellent user experience.

---

**Made with 🌱 for Long Beach Landscaping**
