<?php
/**
 * The main template file
 *
 * @package LongBeach_Landscaping
 */

get_header();
?>

<main class="site-main" style="padding-top: 100px; min-height: 60vh;">
    <div class="container">
        <?php
        if ( have_posts() ) :
            ?>
            <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; padding: 60px 0;">
                <?php
                while ( have_posts() ) :
                    the_post();
                    ?>
                    <article id="post-<?php the_ID(); ?>" <?php post_class( 'blog-post-card' ); ?> style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                        <?php if ( has_post_thumbnail() ) : ?>
                            <div class="post-thumbnail" style="margin-bottom: 20px;">
                                <a href="<?php the_permalink(); ?>">
                                    <?php the_post_thumbnail( 'large', array( 'style' => 'width: 100%; height: auto; border-radius: 5px;' ) ); ?>
                                </a>
                            </div>
                        <?php endif; ?>

                        <h2 class="entry-title" style="margin-bottom: 15px;">
                            <a href="<?php the_permalink(); ?>" style="color: var(--primary-color);">
                                <?php the_title(); ?>
                            </a>
                        </h2>

                        <div class="entry-meta" style="color: var(--text-gray); font-size: 0.9rem; margin-bottom: 15px;">
                            <span><?php echo get_the_date(); ?></span>
                            <span> | </span>
                            <span><?php the_author(); ?></span>
                        </div>

                        <div class="entry-content" style="color: var(--text-gray); line-height: 1.7; margin-bottom: 20px;">
                            <?php the_excerpt(); ?>
                        </div>

                        <a href="<?php the_permalink(); ?>" class="btn btn-primary" style="display: inline-block;">
                            Read More
                        </a>
                    </article>
                    <?php
                endwhile;
                ?>
            </div>

            <?php
            the_posts_navigation();
        else :
            ?>
            <div class="no-posts" style="text-align: center; padding: 100px 20px;">
                <h2>Nothing Found</h2>
                <p>It seems we can't find what you're looking for. Perhaps searching can help.</p>
                <?php get_search_form(); ?>
            </div>
            <?php
        endif;
        ?>
    </div>
</main>

<?php
get_footer();
