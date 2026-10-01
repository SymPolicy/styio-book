import unittest
from check_rendered import Page


class RenderedPageTest(unittest.TestCase):
    def test_pipe_remains_code_text(self):
        page = Page('<code>&lt;| expr</code><code>?(cond) =&gt; { ... } | { ... }</code>')
        self.assertEqual(['<| expr', '?(cond) => { ... } | { ... }'], page.code)

    def test_counts_damaged_table(self):
        page = Page('<table><tr><th>A</th><th>B</th><th>C</th></tr>'
                    '<tr><td>Return</td><td>`&lt;\\</td><td>expr`</td><td>note</td></tr></table>')
        self.assertEqual([3, 4], page.rows)

    def test_reads_anchor_and_asset(self):
        page = Page('<h2 id="forms">Forms</h2><a href="#forms">go</a><img src="plot.png">')
        self.assertEqual({'forms'}, page.ids)
        self.assertEqual(['#forms', 'plot.png'], page.links)
