<?php
/**
 * Single Post Template
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main single-post" style="padding: 120px 0 60px; min-height: 60vh;">
    <div class="container">
        <?php
        while ( have_posts() ) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class( 'single-post-content' ); ?>>

                <?php if ( has_post_thumbnail() ) : ?>
                    <div class="post-thumbnail" style="margin-bottom: 40px; border-radius: 10px; overflow: hidden;">
                        <?php the_post_thumbnail( 'large' ); ?>
                    </div>
                <?php endif; ?>

                <header class="entry-header" style="margin-bottom: 30px;">
                    <h1 class="entry-title" style="color: var(--primary-color); margin-bottom: 15px;">
                        <?php the_title(); ?>
                    </h1>

                    <div class="entry-meta" style="color: var(--text-gray); font-size: 0.95rem;">
                        <span class="posted-on">
                            <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>">
                                <?php echo get_the_date(); ?>
                            </time>
                        </span>
                        <span style="margin: 0 10px;">|</span>
                        <span class="byline">
                            By <?php the_author(); ?>
                        </span>
                        <?php if ( has_category() ) : ?>
                            <span style="margin: 0 10px;">|</span>
                            <span class="cat-links">
                                <?php the_category( ', ' ); ?>
                            </span>
                        <?php endif; ?>
                    </div>
                </header>

                <div class="entry-content" style="max-width: 800px; line-height: 1.8; color: var(--text-gray);">
                    <?php
                    the_content();

                    wp_link_pages( array(
                        'before' => '<div class="page-links">' . esc_html__( 'Pages:', 'longbeach-landscaping' ),
                        'after'  => '</div>',
                    ) );
                    ?>
                </div>

                <?php if ( get_the_tags() ) : ?>
                    <footer class="entry-footer" style="margin-top: 40px; padding-top: 30px; border-top: 1px solid var(--border-color);">
                        <div class="tags-links">
                            <?php the_tags( '<strong>Tags:</strong> ', ', ' ); ?>
                        </div>
                    </footer>
                <?php endif; ?>

            </article>

            <nav class="post-navigation" style="margin-top: 60px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div class="nav-previous" style="text-align: left;">
                    <?php previous_post_link( '%link', '← %title' ); ?>
                </div>
                <div class="nav-next" style="text-align: right;">
                    <?php next_post_link( '%link', '%title →' ); ?>
                </div>
            </nav>

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
