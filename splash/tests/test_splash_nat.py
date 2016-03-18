import re

from splash.tests.test_render import BaseRenderTest
import pytest


@pytest.mark.usefixtures("class_ts_with_logfile")
class SplashNATTest(BaseRenderTest):
    def get_log_content(self):
        with open(self.ts.logfile) as logfile:
            contents = logfile.read()
        return contents

    def test_requests_not_downloaded_after_processing_done(self):
        r = self.request({"url": self.mockurl("requests-after-load")})
        self.assertStatusCode(r, 200)
        finished_downloading = "Headers received.+requests-after-load/other_resource"
        log_content = self.get_log_content()
        self.assertFalse(bool(re.search(finished_downloading, log_content)))
        from IPython import embed; embed()

