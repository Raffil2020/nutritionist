<?php
/**
 * Front Page Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<!-- Hero Section -->
<section class="hero" id="home">
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <h2 class="hero-title"><?php echo esc_html( get_theme_mod( 'longbeach_hero_title', 'Transform Your Outdoor Space' ) ); ?></h2>
        <p class="hero-subtitle"><?php echo esc_html( get_theme_mod( 'longbeach_hero_subtitle', 'Professional Landscaping Services in Long Beach, California' ) ); ?></p>
        <div class="hero-buttons">
            <a href="#portfolio" class="btn btn-primary">View Our Work</a>
            <a href="#contact" class="btn btn-secondary">Free Consultation</a>
        </div>
    </div>
    <div class="scroll-indicator">
        <span></span>
    </div>
</section>

<!-- About Section -->
<section class="about" id="about">
    <div class="container">
        <div class="section-header">
            <h2>About Us</h2>
            <div class="divider"></div>
        </div>
        <div class="about-content">
            <div class="about-image">
                <?php
                $about_page = get_page_by_path( 'about' );
                if ( $about_page && has_post_thumbnail( $about_page->ID ) ) {
                    echo get_the_post_thumbnail( $about_page->ID, 'longbeach-about', array( 'alt' => 'About Long Beach Landscaping' ) );
                } else {
                    ?>
                    <img src="<?php echo get_template_directory_uri(); ?>/images/about-placeholder.jpg" alt="Long Beach Landscaping Team" loading="lazy">
                    <?php
                }
                ?>
            </div>
            <div class="about-text">
                <h3>Creating Beautiful Outdoor Spaces Since 2010</h3>
                <?php
                if ( $about_page ) {
                    echo apply_filters( 'the_content', $about_page->post_content );
                } else {
                    ?>
                    <p>Long Beach Landscaping is your premier choice for professional landscape design, installation, and maintenance services. With over 13 years of experience serving the Long Beach community, we specialize in transforming ordinary outdoor spaces into extraordinary living environments.</p>
                    <p>Our team of certified landscaping professionals combines creativity, expertise, and attention to detail to deliver results that exceed expectations. Whether you're looking for a complete landscape renovation or regular maintenance services, we're committed to bringing your vision to life.</p>
                    <?php
                }
                ?>
                <div class="about-features">
                    <div class="feature-item">
                        <div class="feature-icon">🏆</div>
                        <div class="feature-text">
                            <h4>Award Winning</h4>
                            <p>Recognized for excellence in landscape design</p>
                        </div>
                    </div>
                    <div class="feature-item">
                        <div class="feature-icon">🌱</div>
                        <div class="feature-text">
                            <h4>Eco-Friendly</h4>
                            <p>Sustainable practices and native plants</p>
                        </div>
                    </div>
                    <div class="feature-item">
                        <div class="feature-icon">✓</div>
                        <div class="feature-text">
                            <h4>Licensed & Insured</h4>
                            <p>Fully certified and bonded professionals</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Services Section -->
<section class="services" id="services">
    <div class="container">
        <div class="section-header">
            <h2>Our Services</h2>
            <div class="divider"></div>
            <p class="section-subtitle">Comprehensive landscaping solutions for residential and commercial properties</p>
        </div>
        <div class="services-grid">
            <?php
            $services = new WP_Query( array(
                'post_type'      => 'service',
                'posts_per_page' => 6,
                'orderby'        => 'menu_order',
                'order'          => 'ASC',
            ) );

            if ( $services->have_posts() ) :
                while ( $services->have_posts() ) : $services->the_post();
                    ?>
                    <div class="service-card">
                        <?php if ( has_post_thumbnail() ) : ?>
                            <div class="service-icon">
                                <?php the_post_thumbnail( 'thumbnail' ); ?>
                            </div>
                        <?php endif; ?>
                        <h3><?php the_title(); ?></h3>
                        <?php the_excerpt(); ?>
                    </div>
                    <?php
                endwhile;
                wp_reset_postdata();
            else :
                // Default services if none are added
                ?>
                <div class="service-card">
                    <div class="service-icon">🎨</div>
                    <h3>Landscape Design</h3>
                    <p>Custom outdoor designs tailored to your style, needs, and budget. We create detailed plans that maximize your space's potential.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🔨</div>
                    <h3>Installation</h3>
                    <p>Expert installation of all landscape elements with precision and care, ensuring lasting beauty and functionality.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">💧</div>
                    <h3>Irrigation Systems</h3>
                    <p>Water-efficient irrigation solutions that keep your landscape healthy while conserving resources and reducing costs.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🪨</div>
                    <h3>Hardscaping</h3>
                    <p>Durable and beautiful hardscape features that enhance functionality and add value to your property.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">✂️</div>
                    <h3>Maintenance</h3>
                    <p>Regular maintenance programs to keep your landscape looking its best throughout the year.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon">🌿</div>
                    <h3>Native Plants</h3>
                    <p>California native and drought-tolerant plant installations that thrive in Long Beach's climate.</p>
                </div>
                <?php
            endif;
            ?>
        </div>
    </div>
</section>

<!-- Portfolio Section -->
<section class="portfolio" id="portfolio">
    <div class="container">
        <div class="section-header">
            <h2>Our Portfolio</h2>
            <div class="divider"></div>
            <p class="section-subtitle">Recent projects showcasing our expertise in Long Beach landscaping</p>
        </div>

        <!-- Portfolio Filter -->
        <div class="portfolio-filter">
            <button class="filter-btn active" data-filter="all">All Projects</button>
            <?php
            $portfolio_categories = get_terms( array(
                'taxonomy'   => 'portfolio_category',
                'hide_empty' => true,
            ) );
            if ( ! empty( $portfolio_categories ) && ! is_wp_error( $portfolio_categories ) ) :
                foreach ( $portfolio_categories as $category ) :
                    ?>
                    <button class="filter-btn" data-filter="<?php echo esc_attr( $category->slug ); ?>"><?php echo esc_html( $category->name ); ?></button>
                    <?php
                endforeach;
            else :
                ?>
                <button class="filter-btn" data-filter="residential">Residential</button>
                <button class="filter-btn" data-filter="commercial">Commercial</button>
                <button class="filter-btn" data-filter="hardscape">Hardscape</button>
                <button class="filter-btn" data-filter="maintenance">Maintenance</button>
                <?php
            endif;
            ?>
        </div>

        <!-- Portfolio Grid -->
        <div class="portfolio-grid">
            <?php
            $portfolio = new WP_Query( array(
                'post_type'      => 'portfolio',
                'posts_per_page' => 6,
                'orderby'        => 'date',
                'order'          => 'DESC',
            ) );

            if ( $portfolio->have_posts() ) :
                while ( $portfolio->have_posts() ) : $portfolio->the_post();
                    $categories = wp_get_post_terms( get_the_ID(), 'portfolio_category', array( 'fields' => 'slugs' ) );
                    $category_string = implode( ' ', $categories );
                    ?>
                    <div class="portfolio-item" data-category="<?php echo esc_attr( $category_string ); ?>">
                        <div class="portfolio-image">
                            <?php
                            if ( has_post_thumbnail() ) {
                                the_post_thumbnail( 'longbeach-portfolio', array( 'loading' => 'lazy' ) );
                            } else {
                                ?>
                                <img src="<?php echo get_template_directory_uri(); ?>/images/project-placeholder.jpg" alt="<?php the_title_attribute(); ?>" loading="lazy">
                                <?php
                            }
                            ?>
                            <div class="portfolio-overlay">
                                <h3><?php the_title(); ?></h3>
                                <?php if ( has_excerpt() ) : ?>
                                    <p><?php echo get_the_excerpt(); ?></p>
                                <?php endif; ?>
                                <a href="<?php the_permalink(); ?>" class="btn-view">View Details</a>
                            </div>
                        </div>
                    </div>
                    <?php
                endwhile;
                wp_reset_postdata();
            else :
                // Default portfolio items if none are added
                for ( $i = 1; $i <= 6; $i++ ) :
                    ?>
                    <div class="portfolio-item" data-category="residential">
                        <div class="portfolio-image">
                            <img src="<?php echo get_template_directory_uri(); ?>/images/project<?php echo $i; ?>-placeholder.jpg" alt="Portfolio Project <?php echo $i; ?>" loading="lazy">
                            <div class="portfolio-overlay">
                                <h3>Sample Project <?php echo $i; ?></h3>
                                <p>Long Beach, CA</p>
                                <button class="btn-view">View Details</button>
                            </div>
                        </div>
                    </div>
                    <?php
                endfor;
            endif;
            ?>
        </div>
    </div>
</section>

<!-- Testimonials Section -->
<section class="testimonials" id="testimonials">
    <div class="container">
        <div class="section-header">
            <h2>What Our Clients Say</h2>
            <div class="divider"></div>
        </div>
        <div class="testimonials-slider">
            <div class="testimonial-track">
                <?php
                $testimonials = new WP_Query( array(
                    'post_type'      => 'testimonial',
                    'posts_per_page' => 5,
                    'orderby'        => 'date',
                    'order'          => 'DESC',
                ) );

                if ( $testimonials->have_posts() ) :
                    while ( $testimonials->have_posts() ) : $testimonials->the_post();
                        ?>
                        <div class="testimonial-card">
                            <div class="stars">★★★★★</div>
                            <?php the_content(); ?>
                            <div class="testimonial-author">
                                <h4><?php the_title(); ?></h4>
                                <?php if ( has_excerpt() ) : ?>
                                    <p><?php echo get_the_excerpt(); ?></p>
                                <?php endif; ?>
                            </div>
                        </div>
                        <?php
                    endwhile;
                    wp_reset_postdata();
                else :
                    // Default testimonials
                    ?>
                    <div class="testimonial-card">
                        <div class="stars">★★★★★</div>
                        <p class="testimonial-text">"Long Beach Landscaping transformed our backyard into an absolute paradise! Their attention to detail and professionalism exceeded our expectations. The team was punctual, respectful, and the final result is stunning."</p>
                        <div class="testimonial-author">
                            <h4>Sarah Martinez</h4>
                            <p>Belmont Shore</p>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="stars">★★★★★</div>
                        <p class="testimonial-text">"We hired them for our commercial property, and they've been maintaining it for two years now. Always reliable, always professional. Our property looks amazing year-round, and our clients constantly comment on the beautiful landscaping."</p>
                        <div class="testimonial-author">
                            <h4>Michael Chen</h4>
                            <p>Property Manager, Downtown LB</p>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="stars">★★★★★</div>
                        <p class="testimonial-text">"The custom patio and fire pit they installed has become our favorite place to entertain. The design process was collaborative and fun, and the installation was completed on time and within budget. Highly recommend!"</p>
                        <div class="testimonial-author">
                            <h4>Jennifer & Tom Williams</h4>
                            <p>Naples Island</p>
                        </div>
                    </div>
                    <?php
                endif;
                ?>
            </div>
            <div class="testimonial-controls">
                <button class="testimonial-btn prev" aria-label="Previous testimonial">‹</button>
                <button class="testimonial-btn next" aria-label="Next testimonial">›</button>
            </div>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section class="contact" id="contact">
    <div class="container">
        <div class="section-header">
            <h2>Get In Touch</h2>
            <div class="divider"></div>
            <p class="section-subtitle">Ready to transform your outdoor space? Contact us for a free consultation</p>
        </div>
        <div class="contact-wrapper">
            <div class="contact-info">
                <h3>Contact Information</h3>
                <div class="contact-item">
                    <div class="contact-icon">📍</div>
                    <div>
                        <h4>Address</h4>
                        <p><?php echo wp_kses_post( nl2br( get_theme_mod( 'longbeach_address', '123 Ocean Boulevard<br>Long Beach, CA 90802' ) ) ); ?></p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">📞</div>
                    <div>
                        <h4>Phone</h4>
                        <p><?php echo esc_html( get_theme_mod( 'longbeach_phone', '(562) 555-LAWN' ) ); ?></p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">✉️</div>
                    <div>
                        <h4>Email</h4>
                        <p><?php echo esc_html( get_theme_mod( 'longbeach_email', 'info@longbeachlandscaping.com' ) ); ?></p>
                    </div>
                </div>
                <div class="contact-item">
                    <div class="contact-icon">🕒</div>
                    <div>
                        <h4>Business Hours</h4>
                        <p>Monday - Friday: 7:00 AM - 6:00 PM<br>
                        Saturday: 8:00 AM - 4:00 PM<br>
                        Sunday: Closed</p>
                    </div>
                </div>
                <div class="social-links">
                    <a href="#" aria-label="Facebook">Facebook</a>
                    <a href="#" aria-label="Instagram">Instagram</a>
                    <a href="#" aria-label="Yelp">Yelp</a>
                </div>
            </div>
            <div class="contact-form-wrapper">
                <form class="contact-form" id="contactForm">
                    <div class="form-group">
                        <label for="name">Full Name *</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="tel" id="phone" name="phone">
                    </div>
                    <div class="form-group">
                        <label for="service">Service Interested In</label>
                        <select id="service" name="service">
                            <option value="">Select a service</option>
                            <option value="design">Landscape Design</option>
                            <option value="installation">Installation</option>
                            <option value="irrigation">Irrigation Systems</option>
                            <option value="hardscape">Hardscaping</option>
                            <option value="maintenance">Maintenance</option>
                            <option value="native">Native Plants</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="message">Message *</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary btn-submit">Send Message</button>
                </form>
                <div class="form-message" id="formMessage"></div>
            </div>
        </div>
    </div>
</section>

<?php
get_footer();
