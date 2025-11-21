<?php
/**
 * Search Results Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main search-results" style="padding: 120px 0 60px; min-height: 60vh;">
    <div class="container">

        <header class="page-header" style="text-align: center; margin-bottom: 60px;">
            <h1 class="page-title" style="color: var(--primary-color); font-size: 2.5rem; margin-bottom: 15px;">
                <?php
                printf(
                    esc_html__( 'Search Results for: %s', 'longbeach-landscaping' ),
                    '<span style="color: var(--secondary-color);">' . get_search_query() . '</span>'
                );
                ?>
            </h1>
            <div class="divider" style="margin: 30px auto;"></div>
        </header>

        <?php
        if ( have_posts() ) :
            ?>
            <div class="search-results-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <?php
                while ( have_posts() ) :
                    the_post();
                    ?>
                    <article id="post-<?php the_ID(); ?>" <?php post_class( 'search-result-card' ); ?> style="background: white; padding: 0; border-radius: 10px; box-shadow: var(--shadow-sm); overflow: hidden;">

                        <?php if ( has_post_thumbnail() ) : ?>
                            <div class="post-thumbnail" style="height: 200px; overflow: hidden;">
                                <a href="<?php the_permalink(); ?>">
                                    <?php the_post_thumbnail( 'medium', array( 'style' => 'width: 100%; height: 100%; object-fit: cover;' ) ); ?>
                                </a>
                            </div>
                        <?php endif; ?>

                        <div style="padding: 25px;">
                            <div class="entry-meta" style="color: var(--secondary-color); font-size: 0.85rem; margin-bottom: 10px; text-transform: uppercase; font-weight: 600;">
                                <?php
                                $post_type = get_post_type();
                                echo esc_html( ucfirst( $post_type ) );
                                ?>
                            </div>

                            <h2 class="entry-title" style="font-size: 1.5rem; margin-bottom: 10px;">
                                <a href="<?php the_permalink(); ?>" style="color: var(--primary-color);">
                                    <?php the_title(); ?>
                                </a>
                            </h2>

                            <div class="entry-meta" style="color: var(--text-gray); font-size: 0.85rem; margin-bottom: 15px;">
                                <span><?php echo get_the_date(); ?></span>
                                <span style="margin: 0 5px;">•</span>
                                <span><?php the_author(); ?></span>
                            </div>

                            <div class="entry-excerpt" style="color: var(--text-gray); line-height: 1.6; margin-bottom: 15px;">
                                <?php the_excerpt(); ?>
                            </div>

                            <a href="<?php the_permalink(); ?>" class="btn btn-primary" style="display: inline-block; padding: 10px 20px; font-size: 0.9rem;">
                                <?php esc_html_e( 'View Details', 'longbeach-landscaping' ); ?>
                            </a>
                        </div>
                    </article>
                    <?php
                endwhile;
                ?>
            </div>

            <?php
            the_posts_pagination( array(
                'mid_size'  => 2,
                'prev_text' => __( '← Previous', 'longbeach-landscaping' ),
                'next_text' => __( 'Next →', 'longbeach-landscaping' ),
            ) );

        else :
            ?>
            <div class="no-results" style="text-align: center; padding: 60px 20px; max-width: 600px; margin: 0 auto;">
                <h2 style="color: var(--primary-color); margin-bottom: 20px;">
                    <?php esc_html_e( 'Nothing Found', 'longbeach-landscaping' ); ?>
                </h2>
                <p style="color: var(--text-gray); margin-bottom: 30px; line-height: 1.7;">
                    <?php esc_html_e( 'Sorry, but nothing matched your search terms. Please try again with different keywords.', 'longbeach-landscaping' ); ?>
                </p>

                <div style="margin-bottom: 40px;">
                    <?php get_search_form(); ?>
                </div>

                <div>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn btn-primary">
                        <?php esc_html_e( 'Back to Homepage', 'longbeach-landscaping' ); ?>
                    </a>
                </div>
            </div>
            <?php
        endif;
        ?>
    </div>
</main>

<?php
get_footer();
