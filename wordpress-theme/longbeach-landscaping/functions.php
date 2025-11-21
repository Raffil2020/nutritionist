<?php
/**
 * Long Beach Landscaping Theme Functions
 *
 * @package LongBeach_Landscaping
 */

// Exit if accessed directly
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Theme Setup
 */
function longbeach_landscaping_setup() {
    // Add default posts and comments RSS feed links to head
    add_theme_support( 'automatic-feed-links' );

    // Let WordPress manage the document title
    add_theme_support( 'title-tag' );

    // Enable support for Post Thumbnails
    add_theme_support( 'post-thumbnails' );
    set_post_thumbnail_size( 600, 400, true );
    add_image_size( 'longbeach-portfolio', 600, 400, true );
    add_image_size( 'longbeach-about', 800, 600, true );

    // Register navigation menus
    register_nav_menus( array(
        'primary' => esc_html__( 'Primary Menu', 'longbeach-landscaping' ),
        'footer'  => esc_html__( 'Footer Menu', 'longbeach-landscaping' ),
    ) );

    // Switch default core markup to output valid HTML5
    add_theme_support( 'html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script',
    ) );

    // Add theme support for custom logo
    add_theme_support( 'custom-logo', array(
        'height'      => 100,
        'width'       => 400,
        'flex-height' => true,
        'flex-width'  => true,
    ) );

    // Add theme support for selective refresh for widgets
    add_theme_support( 'customize-selective-refresh-widgets' );

    // Add support for custom backgrounds
    add_theme_support( 'custom-background', array(
        'default-color' => 'ffffff',
    ) );

    // Add support for editor styles
    add_theme_support( 'editor-styles' );
}
add_action( 'after_setup_theme', 'longbeach_landscaping_setup' );

/**
 * Set the content width
 */
function longbeach_landscaping_content_width() {
    $GLOBALS['content_width'] = apply_filters( 'longbeach_landscaping_content_width', 1200 );
}
add_action( 'after_setup_theme', 'longbeach_landscaping_content_width', 0 );

/**
 * Register widget areas
 */
function longbeach_landscaping_widgets_init() {
    register_sidebar( array(
        'name'          => esc_html__( 'Footer Column 1', 'longbeach-landscaping' ),
        'id'            => 'footer-1',
        'description'   => esc_html__( 'Add widgets here for first footer column.', 'longbeach-landscaping' ),
        'before_widget' => '<div id="%1$s" class="footer-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ) );

    register_sidebar( array(
        'name'          => esc_html__( 'Footer Column 2', 'longbeach-landscaping' ),
        'id'            => 'footer-2',
        'description'   => esc_html__( 'Add widgets here for second footer column.', 'longbeach-landscaping' ),
        'before_widget' => '<div id="%1$s" class="footer-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ) );

    register_sidebar( array(
        'name'          => esc_html__( 'Footer Column 3', 'longbeach-landscaping' ),
        'id'            => 'footer-3',
        'description'   => esc_html__( 'Add widgets here for third footer column.', 'longbeach-landscaping' ),
        'before_widget' => '<div id="%1$s" class="footer-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ) );

    register_sidebar( array(
        'name'          => esc_html__( 'Footer Column 4', 'longbeach-landscaping' ),
        'id'            => 'footer-4',
        'description'   => esc_html__( 'Add widgets here for fourth footer column.', 'longbeach-landscaping' ),
        'before_widget' => '<div id="%1$s" class="footer-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h4 class="widget-title">',
        'after_title'   => '</h4>',
    ) );
}
add_action( 'widgets_init', 'longbeach_landscaping_widgets_init' );

/**
 * Enqueue scripts and styles
 */
function longbeach_landscaping_scripts() {
    // Google Fonts
    wp_enqueue_style( 'longbeach-google-fonts', 'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Open+Sans:wght@400;600&display=swap', array(), null );

    // Theme stylesheet
    wp_enqueue_style( 'longbeach-landscaping-style', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );

    // Theme JavaScript
    wp_enqueue_script( 'longbeach-landscaping-script', get_template_directory_uri() . '/js/script.js', array(), wp_get_theme()->get( 'Version' ), true );

    // Localize script for AJAX
    wp_localize_script( 'longbeach-landscaping-script', 'longbeachAjax', array(
        'ajaxurl' => admin_url( 'admin-ajax.php' ),
        'nonce'   => wp_create_nonce( 'longbeach_nonce' ),
    ) );
}
add_action( 'wp_enqueue_scripts', 'longbeach_landscaping_scripts' );

/**
 * Register Custom Post Type - Portfolio
 */
function longbeach_register_portfolio_post_type() {
    $labels = array(
        'name'               => _x( 'Portfolio', 'post type general name', 'longbeach-landscaping' ),
        'singular_name'      => _x( 'Portfolio Item', 'post type singular name', 'longbeach-landscaping' ),
        'menu_name'          => _x( 'Portfolio', 'admin menu', 'longbeach-landscaping' ),
        'name_admin_bar'     => _x( 'Portfolio Item', 'add new on admin bar', 'longbeach-landscaping' ),
        'add_new'            => _x( 'Add New', 'portfolio item', 'longbeach-landscaping' ),
        'add_new_item'       => __( 'Add New Portfolio Item', 'longbeach-landscaping' ),
        'new_item'           => __( 'New Portfolio Item', 'longbeach-landscaping' ),
        'edit_item'          => __( 'Edit Portfolio Item', 'longbeach-landscaping' ),
        'view_item'          => __( 'View Portfolio Item', 'longbeach-landscaping' ),
        'all_items'          => __( 'All Portfolio Items', 'longbeach-landscaping' ),
        'search_items'       => __( 'Search Portfolio Items', 'longbeach-landscaping' ),
        'not_found'          => __( 'No portfolio items found.', 'longbeach-landscaping' ),
        'not_found_in_trash' => __( 'No portfolio items found in Trash.', 'longbeach-landscaping' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'portfolio' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => 5,
        'menu_icon'          => 'dashicons-portfolio',
        'supports'           => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
    );

    register_post_type( 'portfolio', $args );
}
add_action( 'init', 'longbeach_register_portfolio_post_type' );

/**
 * Register Custom Taxonomy - Portfolio Category
 */
function longbeach_register_portfolio_taxonomy() {
    $labels = array(
        'name'              => _x( 'Portfolio Categories', 'taxonomy general name', 'longbeach-landscaping' ),
        'singular_name'     => _x( 'Portfolio Category', 'taxonomy singular name', 'longbeach-landscaping' ),
        'search_items'      => __( 'Search Portfolio Categories', 'longbeach-landscaping' ),
        'all_items'         => __( 'All Portfolio Categories', 'longbeach-landscaping' ),
        'parent_item'       => __( 'Parent Portfolio Category', 'longbeach-landscaping' ),
        'parent_item_colon' => __( 'Parent Portfolio Category:', 'longbeach-landscaping' ),
        'edit_item'         => __( 'Edit Portfolio Category', 'longbeach-landscaping' ),
        'update_item'       => __( 'Update Portfolio Category', 'longbeach-landscaping' ),
        'add_new_item'      => __( 'Add New Portfolio Category', 'longbeach-landscaping' ),
        'new_item_name'     => __( 'New Portfolio Category Name', 'longbeach-landscaping' ),
        'menu_name'         => __( 'Portfolio Categories', 'longbeach-landscaping' ),
    );

    $args = array(
        'hierarchical'      => true,
        'labels'            => $labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'portfolio-category' ),
    );

    register_taxonomy( 'portfolio_category', array( 'portfolio' ), $args );
}
add_action( 'init', 'longbeach_register_portfolio_taxonomy' );

/**
 * Register Custom Post Type - Services
 */
function longbeach_register_services_post_type() {
    $labels = array(
        'name'               => _x( 'Services', 'post type general name', 'longbeach-landscaping' ),
        'singular_name'      => _x( 'Service', 'post type singular name', 'longbeach-landscaping' ),
        'menu_name'          => _x( 'Services', 'admin menu', 'longbeach-landscaping' ),
        'name_admin_bar'     => _x( 'Service', 'add new on admin bar', 'longbeach-landscaping' ),
        'add_new'            => _x( 'Add New', 'service', 'longbeach-landscaping' ),
        'add_new_item'       => __( 'Add New Service', 'longbeach-landscaping' ),
        'new_item'           => __( 'New Service', 'longbeach-landscaping' ),
        'edit_item'          => __( 'Edit Service', 'longbeach-landscaping' ),
        'view_item'          => __( 'View Service', 'longbeach-landscaping' ),
        'all_items'          => __( 'All Services', 'longbeach-landscaping' ),
        'search_items'       => __( 'Search Services', 'longbeach-landscaping' ),
        'not_found'          => __( 'No services found.', 'longbeach-landscaping' ),
        'not_found_in_trash' => __( 'No services found in Trash.', 'longbeach-landscaping' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array( 'slug' => 'services' ),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => 6,
        'menu_icon'          => 'dashicons-admin-tools',
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
    );

    register_post_type( 'service', $args );
}
add_action( 'init', 'longbeach_register_services_post_type' );

/**
 * Register Custom Post Type - Testimonials
 */
function longbeach_register_testimonials_post_type() {
    $labels = array(
        'name'               => _x( 'Testimonials', 'post type general name', 'longbeach-landscaping' ),
        'singular_name'      => _x( 'Testimonial', 'post type singular name', 'longbeach-landscaping' ),
        'menu_name'          => _x( 'Testimonials', 'admin menu', 'longbeach-landscaping' ),
        'add_new_item'       => __( 'Add New Testimonial', 'longbeach-landscaping' ),
        'edit_item'          => __( 'Edit Testimonial', 'longbeach-landscaping' ),
        'all_items'          => __( 'All Testimonials', 'longbeach-landscaping' ),
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'capability_type'    => 'post',
        'hierarchical'       => false,
        'menu_position'      => 7,
        'menu_icon'          => 'dashicons-star-filled',
        'supports'           => array( 'title', 'editor', 'thumbnail' ),
    );

    register_post_type( 'testimonial', $args );
}
add_action( 'init', 'longbeach_register_testimonials_post_type' );

/**
 * Contact Form Handler
 */
function longbeach_handle_contact_form() {
    check_ajax_referer( 'longbeach_nonce', 'nonce' );

    $name = sanitize_text_field( $_POST['name'] );
    $email = sanitize_email( $_POST['email'] );
    $phone = sanitize_text_field( $_POST['phone'] );
    $service = sanitize_text_field( $_POST['service'] );
    $message = sanitize_textarea_field( $_POST['message'] );

    // Validate required fields
    if ( empty( $name ) || empty( $email ) || empty( $message ) ) {
        wp_send_json_error( array( 'message' => 'Please fill in all required fields.' ) );
    }

    // Validate email
    if ( ! is_email( $email ) ) {
        wp_send_json_error( array( 'message' => 'Please enter a valid email address.' ) );
    }

    // Prepare email
    $to = get_option( 'admin_email' );
    $subject = 'New Contact Form Submission from ' . $name;
    $body = "Name: $name\n";
    $body .= "Email: $email\n";
    $body .= "Phone: $phone\n";
    $body .= "Service: $service\n\n";
    $body .= "Message:\n$message";

    $headers = array( 'Content-Type: text/plain; charset=UTF-8' );

    // Send email
    if ( wp_mail( $to, $subject, $body, $headers ) ) {
        wp_send_json_success( array( 'message' => 'Thank you for your message! We will get back to you soon.' ) );
    } else {
        wp_send_json_error( array( 'message' => 'Sorry, there was an error sending your message. Please try again.' ) );
    }
}
add_action( 'wp_ajax_longbeach_contact_form', 'longbeach_handle_contact_form' );
add_action( 'wp_ajax_nopriv_longbeach_contact_form', 'longbeach_handle_contact_form' );

/**
 * Customizer Settings
 */
function longbeach_customize_register( $wp_customize ) {
    // Add Hero Section
    $wp_customize->add_section( 'longbeach_hero', array(
        'title'    => __( 'Hero Section', 'longbeach-landscaping' ),
        'priority' => 30,
    ) );

    // Hero Title
    $wp_customize->add_setting( 'longbeach_hero_title', array(
        'default'           => 'Transform Your Outdoor Space',
        'sanitize_callback' => 'sanitize_text_field',
    ) );

    $wp_customize->add_control( 'longbeach_hero_title', array(
        'label'   => __( 'Hero Title', 'longbeach-landscaping' ),
        'section' => 'longbeach_hero',
        'type'    => 'text',
    ) );

    // Hero Subtitle
    $wp_customize->add_setting( 'longbeach_hero_subtitle', array(
        'default'           => 'Professional Landscaping Services in Long Beach, California',
        'sanitize_callback' => 'sanitize_text_field',
    ) );

    $wp_customize->add_control( 'longbeach_hero_subtitle', array(
        'label'   => __( 'Hero Subtitle', 'longbeach-landscaping' ),
        'section' => 'longbeach_hero',
        'type'    => 'text',
    ) );

    // Contact Information Section
    $wp_customize->add_section( 'longbeach_contact', array(
        'title'    => __( 'Contact Information', 'longbeach-landscaping' ),
        'priority' => 40,
    ) );

    // Address
    $wp_customize->add_setting( 'longbeach_address', array(
        'default'           => '123 Ocean Boulevard, Long Beach, CA 90802',
        'sanitize_callback' => 'sanitize_textarea_field',
    ) );

    $wp_customize->add_control( 'longbeach_address', array(
        'label'   => __( 'Address', 'longbeach-landscaping' ),
        'section' => 'longbeach_contact',
        'type'    => 'textarea',
    ) );

    // Phone
    $wp_customize->add_setting( 'longbeach_phone', array(
        'default'           => '(562) 555-LAWN',
        'sanitize_callback' => 'sanitize_text_field',
    ) );

    $wp_customize->add_control( 'longbeach_phone', array(
        'label'   => __( 'Phone Number', 'longbeach-landscaping' ),
        'section' => 'longbeach_contact',
        'type'    => 'text',
    ) );

    // Email
    $wp_customize->add_setting( 'longbeach_email', array(
        'default'           => 'info@longbeachlandscaping.com',
        'sanitize_callback' => 'sanitize_email',
    ) );

    $wp_customize->add_control( 'longbeach_email', array(
        'label'   => __( 'Email', 'longbeach-landscaping' ),
        'section' => 'longbeach_contact',
        'type'    => 'email',
    ) );
}
add_action( 'customize_register', 'longbeach_customize_register' );

/**
 * Excerpt Length
 */
function longbeach_excerpt_length( $length ) {
    return 30;
}
add_filter( 'excerpt_length', 'longbeach_excerpt_length' );

/**
 * Excerpt More
 */
function longbeach_excerpt_more( $more ) {
    return '...';
}
add_filter( 'excerpt_more', 'longbeach_excerpt_more' );
