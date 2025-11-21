<?php
/**
 * Archive Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main archive-page" style="padding: 120px 0 60px; min-height: 60vh;">
    <div class="container">

        <header class="page-header" style="text-align: center; margin-bottom: 60px;">
            <?php
            the_archive_title( '<h1 class="page-title" style="color: var(--primary-color); font-size: 2.5rem; margin-bottom: 15px;">', '</h1>' );
            the_archive_description( '<div class="archive-description" style="color: var(--text-gray); max-width: 700px; margin: 0 auto;">', '</div>' );
            ?>
            <div class="divider" style="margin: 30px auto;"></div>
        </header>

        <?php
        if ( have_posts() ) :
            ?>
            <div class="archive-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <?php
                while ( have_posts() ) :
                    the_post();
                    ?>
                    <article id="post-<?php the_ID(); ?>" <?php post_class( 'archive-post-card' ); ?> style="background: white; padding: 0; border-radius: 10px; box-shadow: var(--shadow-sm); overflow: hidden; transition: var(--transition);">

                        <?php if ( has_post_thumbnail() ) : ?>
                            <div class="post-thumbnail" style="height: 200px; overflow: hidden;">
                                <a href="<?php the_permalink(); ?>">
                                    <?php the_post_thumbnail( 'medium', array( 'style' => 'width: 100%; height: 100%; object-fit: cover;' ) ); ?>
                                </a>
                            </div>
                        <?php endif; ?>

                        <div style="padding: 25px;">
                            <h2 class="entry-title" style="font-size: 1.5rem; margin-bottom: 10px;">
                                <a href="<?php the_permalink(); ?>" style="color: var(--primary-color);">
                                    <?php the_title(); ?>
                                </a>
                            </h2>

                            <div class="entry-meta" style="color: var(--text-gray); font-size: 0.85rem; margin-bottom: 15px;">
                                <span><?php echo get_the_date(); ?></span>
                            </div>

                            <div class="entry-excerpt" style="color: var(--text-gray); line-height: 1.6; margin-bottom: 15px;">
                                <?php the_excerpt(); ?>
                            </div>

                            <a href="<?php the_permalink(); ?>" class="btn btn-primary" style="display: inline-block; padding: 10px 20px; font-size: 0.9rem;">
                                <?php esc_html_e( 'Read More', 'longbeach-landscaping' ); ?>
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
            <div class="no-posts" style="text-align: center; padding: 60px 20px;">
                <h2 style="color: var(--primary-color); margin-bottom: 20px;">
                    <?php esc_html_e( 'Nothing Found', 'longbeach-landscaping' ); ?>
                </h2>
                <p style="color: var(--text-gray); margin-bottom: 30px;">
                    <?php esc_html_e( 'No posts were found in this archive.', 'longbeach-landscaping' ); ?>
                </p>
                <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="btn btn-primary">
                    <?php esc_html_e( 'Back to Homepage', 'longbeach-landscaping' ); ?>
                </a>
            </div>
            <?php
        endif;
        ?>
    </div>
</main>

<?php
get_footer();
