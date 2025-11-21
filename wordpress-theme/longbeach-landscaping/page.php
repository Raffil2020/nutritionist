<?php
/**
 * Page Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main page-content" style="padding: 120px 0 60px; min-height: 60vh;">
    <div class="container">
        <?php
        while ( have_posts() ) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

                <?php if ( has_post_thumbnail() ) : ?>
                    <div class="page-thumbnail" style="margin-bottom: 40px; border-radius: 10px; overflow: hidden;">
                        <?php the_post_thumbnail( 'large' ); ?>
                    </div>
                <?php endif; ?>

                <header class="entry-header" style="margin-bottom: 40px; text-align: center;">
                    <h1 class="entry-title" style="color: var(--primary-color);">
                        <?php the_title(); ?>
                    </h1>
                    <div class="divider" style="margin: 20px auto;"></div>
                </header>

                <div class="entry-content" style="max-width: 900px; margin: 0 auto; line-height: 1.8; color: var(--text-gray);">
                    <?php
                    the_content();

                    wp_link_pages( array(
                        'before' => '<div class="page-links">' . esc_html__( 'Pages:', 'longbeach-landscaping' ),
                        'after'  => '</div>',
                    ) );
                    ?>
                </div>

            </article>

            <?php
            // If comments are open or we have at least one comment, load up the comment template.
            if ( comments_open() || get_comments_number() ) :
                comments_template();
            endif;

        endwhile;
        ?>
    </div>
</main>

<?php
get_footer();
