<?php
/**
 * 404 Error Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main error-404" style="padding: 120px 0 100px; min-height: 70vh;">
    <div class="container">
        <div class="error-content" style="text-align: center; max-width: 700px; margin: 0 auto;">

            <div style="font-size: 120px; color: var(--primary-color); font-weight: 700; line-height: 1;">
                404
            </div>

            <div class="divider" style="margin: 30px auto;"></div>

            <h1 style="font-size: 2.5rem; color: var(--primary-dark); margin-bottom: 20px;">
                <?php esc_html_e( 'Oops! Page Not Found', 'longbeach-landscaping' ); ?>
            </h1>

            <p style="font-size: 1.2rem; color: var(--text-gray); margin-bottom: 40px; line-height: 1.7;">
                <?php esc_html_e( 'The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.', 'longbeach-landscaping' ); ?>
            </p>

            <div style="margin-bottom: 50px;">
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn btn-primary" style="margin-right: 15px;">
                    <?php esc_html_e( 'Go to Homepage', 'longbeach-landscaping' ); ?>
                </a>
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>#contact" class="btn btn-secondary" style="border-color: var(--primary-color); color: var(--primary-color);">
                    <?php esc_html_e( 'Contact Us', 'longbeach-landscaping' ); ?>
                </a>
            </div>

            <div class="search-form" style="max-width: 500px; margin: 0 auto;">
                <h3 style="color: var(--primary-color); margin-bottom: 20px;">
                    <?php esc_html_e( 'Try Searching:', 'longbeach-landscaping' ); ?>
                </h3>
                <?php get_search_form(); ?>
            </div>

            <div style="margin-top: 50px;">
                <h3 style="color: var(--primary-color); margin-bottom: 20px;">
                    <?php esc_html_e( 'Quick Links:', 'longbeach-landscaping' ); ?>
                </h3>
                <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>#about" style="color: var(--primary-color);">About Us</a>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>#services" style="color: var(--primary-color);">Services</a>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>#portfolio" style="color: var(--primary-color);">Portfolio</a>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>#contact" style="color: var(--primary-color);">Contact</a>
                </div>
            </div>

        </div>
    </div>
</main>

<?php
get_footer();
