from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("test_user", "Instagram", 1000, "photo")

    def test_correct_initialization(self):
        self.assertEqual(self.social_media._username, "test_user")
        self.assertEqual(self.social_media._platform, "Instagram")
        self.assertEqual(self.social_media._followers, 1000)
        self.assertEqual(self.social_media._content_type, "photo")
        self.assertEqual(self.social_media._posts, [])

    def test_platform_property_validation(self):
        self.assertEqual(self.social_media.platform, "Instagram")

    def test_platform_property_raises_error(self):
        expected_message = "Platform should be one of ['Instagram', 'YouTube', 'Twitter']"

        with self.assertRaises(ValueError) as ve:
            SocialMedia("test_user", "InvalidPlatform", 1000, "photo")

        self.assertEqual(expected_message, str(ve.exception))

    def test_followers_validation_raises_error(self):
        expected_message = "Followers cannot be negative."
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -100

        self.assertEqual(expected_message, str(ve.exception))

    def test_create_post(self):

        expected_message = "New photo post created by test_user on Instagram."
        post_content = "Test post"

        result = self.social_media.create_post(post_content)
        self.assertEqual(expected_message, result)
        self.assertEqual([{'content': 'Test post', 'likes': 0, 'comments': []}], self.social_media._posts)


    def test_like_post(self):
        # Test liking a post
        self.social_media.create_post("Test post")
        like_message = self.social_media.like_post(0)
        self.assertEqual(self.social_media._posts[0]['likes'], 1)
        self.assertIn("Post liked by test_user.", like_message)

        # Test liking a post beyond the maximum likes
        for _ in range(10):
            self.social_media.like_post(0)
        like_message = self.social_media.like_post(0)
        self.assertIn("Post has reached the maximum number of likes.", like_message)

        # Test liking an invalid post index
        invalid_like_message = self.social_media.like_post(1)
        self.assertEqual(invalid_like_message, "Invalid post index.")

    def test_comment_on_post(self):
        # Test commenting on a post
        self.social_media.create_post("Test post")
        comment_message = self.social_media.comment_on_post(0, "Great post!")
        self.assertEqual(len(self.social_media._posts[0]['comments']), 1)
        self.assertIn("Comment added by test_user on the post.", comment_message)

        # Test commenting with a short comment
        short_comment_message = self.social_media.comment_on_post(0, "Short")
        self.assertEqual(short_comment_message, "Comment should be more than 10 characters.")

        # Test commenting on an invalid post index
        # invalid_comment_message = self.social_media.comment_on_post(1, "Great post!")
        # self.assertEqual(invalid_comment_message, "IndexError: list index out of range")


if __name__ == "__main__":
    main()
