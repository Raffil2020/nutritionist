<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- Navigation -->
<nav class="navbar" id="navbar">
    <div class="container">
        <div class="nav-wrapper">
            <div class="logo">
                <?php
                if ( has_custom_logo() ) {
                    the_custom_logo();
                } else {
                    ?>
                    <h1><a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php bloginfo( 'name' ); ?></a></h1>
                    <?php
                    $description = get_bloginfo( 'description', 'display' );
                    if ( $description || is_customize_preview() ) :
                        ?>
                        <p class="tagline"><?php echo esc_html( $description ); ?></p>
                    <?php endif; ?>
                    <?php
                }
                ?>
            </div>
            <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <?php
            if ( has_nav_menu( 'primary' ) ) {
                wp_nav_menu( array(
                    'theme_location' => 'primary',
                    'menu_id'        => 'navMenu',
                    'menu_class'     => 'nav-menu',
                    'container'      => false,
                    'fallback_cb'    => false,
                ) );
            } else {
                ?>
                <ul class="nav-menu" id="navMenu">
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#home">Home</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#about">About</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#services">Services</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#portfolio">Portfolio</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#testimonials">Testimonials</a></li>
                    <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>#contact" class="btn-nav">Get Quote</a></li>
                </ul>
                <?php
            }
            ?>
        </div>
    </div>
</nav>
