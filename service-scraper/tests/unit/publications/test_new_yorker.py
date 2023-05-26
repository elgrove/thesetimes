from datetime import datetime

import pytest
from thesetimes_orm.models import Article

from core.article_scraper import ArticleToScrape
from core.publication.new_yorker import TheNewYorker
from tests.cases.publications.new_yorker.article import ARTICLE_HTML
from tests.cases.publications.new_yorker.homepage import HOMEPAGE_HTML


import pytest
from sqlalchemy import create_mock_engine


class MockNewYorkerDriver:
    """Mocking the webdriver service, returning pages from the FT."""

    def __init__(self):
        """Initialise."""
        self.page_source = ""

    def get(self, url):
        """Mock webdriver.get method."""
        if url.endswith("newyorker.com"):
            self.page_source = HOMEPAGE_HTML
        else:
            self.page_source = ARTICLE_HTML


@pytest.mark.unit
class TestNewYorker:
    """Tests for the New Yorker scraper."""

    def test_get_articles_isobject_article(self):
        """Test get_articles."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert all(isinstance(article, ArticleToScrape) for article in articles)

    def test_get_articles_count(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert len(articles) == 9

    def test_get_articles_urls(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        articles = pub.get_articles(driver)

        assert articles == [
            ArticleToScrape(url=url, page_rank=i)
            for i, url in enumerate(
                [
                    "https://www.newyorker.com/magazine/2023/05/29/stephen-satterfield-puts-black-cuisine-at-the-center-of-us-history",
                    "https://www.newyorker.com/news/letter-from-bidens-washington/it-was-more-than-a-desaster",
                    "https://www.newyorker.com/culture/postscript/the-untouchable-tina-turner",
                    "https://www.newyorker.com/culture/culture-desk/david-choes-fans-want-to-follow-him-to-a-world-beyond-conformity",
                    "https://www.newyorker.com/culture/cultural-comment/farewell-kendall-roy-succession",
                    "https://www.newyorker.com/news/daily-comment/how-warhol-turned-the-supreme-court-justices-into-art-critics",
                    "https://www.newyorker.com/magazine/2023/05/29/what-we-owe-our-trees",
                    "https://www.newyorker.com/news/q-and-a/why-masha-gessen-resigned-from-the-pen-america-board",
                    "https://www.newyorker.com/books/under-review/can-you-love-the-art-and-hate-the-artist",
                ],
                start=1,
            )
        ]

    def test_get_article_authors(self):
        """Test get article authors."""
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        authors = pub.get_article_authors(driver, "url")
        assert authors == "Amanda Petrusich"

    def test_get_article_pubdate(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        pubdate = pub.get_article_pubdate(driver, "url")
        assert pubdate == datetime(2023, 5, 25, 18, 37, 21)

    def test_get_article_title(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        title = pub.get_article_title(driver, "url")
        assert title == "The Untouchable Tina Turner"

    def test_get_article_body(self):
        pub = TheNewYorker()
        driver = MockNewYorkerDriver()
        body = pub.get_article_body(driver, "url")
        assert body == [
            "On Wednesday, one of the great American voices—gritty, vehement, tender, and red-hot, containing, somehow, both the entire history and future of rock and roll—went silent. Tina Turner, who was born Anna Mae Bullock, in 1939, in Brownsville, Tennessee, died at her home in Switzerland, at age eighty-three. She was known for her superhuman resilience, and, in a way, I came to believe that she was actually invincible. In 1988, when she was forty-eight years old, she performed to some hundred and eighty thousand fans in Rio de Janeiro, ousting Frank Sinatra from the record books by drawing what was, at that point, the largest-ever ticketed crowd for a solo performer. The show was filmed, thank heavens. The energy is uncanny. Bionic. It’s like watching an Olympic final in Being Badass. Early in the set, wearing a fringed minidress, heeled ankle boots, and a pearl necklace, Turner performs “Better Be Good to Me,” a single from 1984. It’s a song about being in love with someone you don’t entirely trust. “Should I be fractured by your lack of devotion?” she wonders in the first verse. The next bit contains all of her magic. She’s asking a question, but her tone isn’t earnest, it’s incredulous. How dare this person expect her to compromise? “Should I? Should I?” she roars. You will want to holler “NO!” at your screen—but, of course, the question was always rhetorical.",
            "Turner was brought up on a cotton farm and educated in a segregated, one-room schoolhouse. She grew up singing in the choir of the Spring Hill Baptist Church in Nutbush, about sixty miles northeast of Memphis. Her great-great-grandfather, Logan Currie, Sr., had been enslaved in the same region. “I hated the cotton field,” she told Henry Louis Gates, Jr., in a 2007 interview for PBS. “There were those hairy worms crawling, the spiders.” Turner later moved to St. Louis, where she met Ike Turner at the Manhattan Club, a Black bar and venue. She eventually persuaded Ike to let her sing with his band, the Kings of Rhythm. They became romantically involved, and, in 1960, formed the Ike & Tina Turner Revue, becoming hugely popular on the Chitlin’ Circuit, a series of Black-owned night clubs throughout the southeast. In 1971, they had a crossover hit with their cover of Creedence Clearwater Revival’s “Proud Mary,” and performed the song on “The Ed Sullivan Show.” For the broadcast, Turner wears a gold flapper dress. She bounces around the stage vigorously, so gleeful and open and strong that it feels as though, surely, she must have an extra set of lungs stashed somewhere. There’s a looseness to her performance that’s far funkier and more human than the hyper-choreographed, steel-eyed stylings of her modern counterparts. I don’t know how to describe it. She is simply very, very alive.",
            "It’s still hard to write about the sixteen years she spent in that abusive, ugly relationship with Ike. She escaped the marriage in 1976. She was thirty-seven years old, and in possession of just thirty-six cents and a Mobil gasoline card. “I didn’t fear him killing me when I left, because I was already dead,” she told People, in 1981. It was the first time that she had spoken publicly about the abuse, and she described it as “torture.” Besides the usual subjugations (beating and berating her), Ike had changed her name and assumed control of her career and finances. It’s easy to think of this experience as the defining trauma of Turner’s life and art—to presume that it shaped and informed her music in a deep and irrefutable way—but it feels stupid, even unfair, to give Ike, who died of a cocaine overdose in 2007, any more air in her story. There have been two memoirs, a Broadway musical, a feature film, interviews. Turner was asked to confront and remember her abuse for decades after it ended. It feels proper to free her of it now. “I don’t like to pull out old clothes,” Turner said in “Tina,” an HBO documentary from 2021. “It’s like old memories, you just want to leave that in the past.”",
            "Let us look, then, to the nineteen-eighties, a decade in which Turner, liberated from her marriage, dominated the charts and the national imagination: the voice, the power, the presence, the legs, the wardrobe, the hair. My God, the dancing! How free does a person have to be to move that way? Freer than I have ever felt or been, certainly. Some people perform music; some people become music. If you’re having a miserable day, one foolproof cure is typing “Tina Turner live 1985” into the YouTube search bar, and bearing witness to something virtuosic, if not divinely ordained. At the time, Turner was on tour in support of the multiplatinum “Private Dancer,” her fifth full-length album, and the record that resuscitated and then ignited her solo career. There’s some extraordinary footage of David Bowie joining her onstage at a show in Birmingham, England, for a duet of “Tonight,” a song first released on Iggy Pop’s “Lust for Life,” in 1977. Bowie, who co-wrote the track—it features a repeating Aretha Franklin sample—appears on the original; he went on to record it for an album of his own, in 1984. Turner guested on Bowie’s version (they skipped Pop’s spoken-word intro, which describes a heroin overdose). Watching them do it live is electrifying. Bowie is grinning so much and so wildly that I wonder how he even manages to keep on singing. They slow dance for a bit in the middle, while Tim Cappello plays a shirtless saxophone solo. I would call this section “steamy,” but it feels like too chaste of a word. “This is a privilege,” Bowie says, when it’s all over. Boy, does he mean it.",
            "Turner’s later years were appropriately lavish. After she retired, she lived in Küsnacht, Switzerland, in an estate known as the Chateau Algonquin, with clear views of Lake Zurich, and, according to a 2019 profile in the Times, “a life-size two-legged horse sculpture suspended from a domed ceiling, a framed rendering of Turner as an Egyptian queen, a room stuffed with gilded Louis XIV style sofas.” A plaque on the gate announces that, of course, no deliveries should be attempted before noon. Who would dare? Turner stopped performing in 2009, freeing herself of a substantial burden: “I was just tired of singing and making everybody happy,” she said. “That’s all I’d ever done in my life.” How glorious that must have felt—having only to worry about her own joy.",
            "I was having lunch in Chinatown with friends when the news was announced. I had ordered a glass of white wine—indulgent for a weekday afternoon, I suppose, but I was feeling a little indulgent. I experienced a quick pang in my gut when one of my companions announced that Turner had died—the sharp, needling ache that comes when someone who you didn’t know personally, but who you understood to have contributed, in a profound and robust way, to the general goodness of the world, had left it. I swallowed the last of my drink. It felt right to be a little unsteady in that moment. “Tina would have had the wine,” the group chat later confirmed. Did Turner even drink? Who cares? The point was that she found a way to tap into some deep wellspring of ease and abandon and self-love, and drew from it when she needed to. And now she has left that for us, in her music, in her voice, in the singular way she occupied a stage. In this sense, she is untouchable, forever.\xa0♦",
        ]
