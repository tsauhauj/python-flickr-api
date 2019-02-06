import flickr_api as f
import unittest


class TestUpload(unittest.TestCase):
    def test_parse_inline_sizes(self):
        self.maxDiff = None
        sizes = f.objects._parse_inline_sizes({
            'title':
            'Noir comme le soleil',
            'owner':
            f.objects.Person(id="qwerty", token="abcde"),
            'id':
            16180339,
            'ispublic':
            True,
            'isfriend':
            False,
            'isfamily':
            False,
            'url_c':
            'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_c.jpg',
            'height_c':
            534,
            'width_c':
            '800',
            'url_l':
            'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_b.jpg',
            'height_l':
            '684',
            'width_l':
            '1024',
            'url_o':
            'https://farm5.staticflickr.com/X/46284324564_2baac8acd5_o.jpg',
            'height_o':
            '4016',
            'width_o':
            '6016',
            'media':
            'photo',
        })
        self.assertEqual({
            'Original': {
                'label':
                'Original',
                'width':
                '6016',
                'height':
                '4016',
                'source':
                'https://farm5.staticflickr.com/X/46284324564_2baac8acd5_o.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/o/',
                'media':
                'photo'
            },
            'Medium 800': {
                'label':
                'Medium 800',
                'width':
                '800',
                'height':
                534,
                'source':
                'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_c.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/c/',
                'media':
                'photo'
            },
            'Large': {
                'label':
                'Large',
                'width':
                '1024',
                'height':
                '684',
                'source':
                'https://farm5.staticflickr.com/X/46284324564_0a1bf6145a_b.jpg',
                'url':
                'https://www.flickr.com/photos/qwerty/16180339/sizes/l/',
                'media':
                'photo'
            },
        }, sizes)
