from dictcom.models import Word, Definition

container = """
<div class="source-box">
    <div class="def-list">
    {}
    </div>
</div>
"""

data = [
    {
        'html': container.format("""
    <section class="def-pbk">
        <header class="luna-data-header">
            <span class="dbox-pg"><span>pos</span></span> <span>(</span><span class="dbox-bold"><span><span>some kind,</span> <span>of pos</span></span></span><span>)</span>
        </header>
        <div class="def-set">
            <span class="def-number">5</span>
            <div class="def-content">
                <span>the</span> <span>def</span> <span>really</span> <span>1</span>
                <div class="def-block def-inline-example">
                    <span class="dbox-example"><span><span>the</span> <span>example</span> <span>1</span></span></span>
                </div>
            </div>
        </div>
        <div class="def-set">
            <span class="def-number">5</span>
            <div class="def-content">
                <span>the</span> <span>def</span> <span>really</span> <span>2</span>
            </div>
        </div>
    </section>



    <section class="def-pbk">
        <header class="luna-data-header">
            <span class="dbox-pg"><span>pos2</span></span>
        </header>
        <div class="def-set">
            <span class="def-number">5</span>
            <div class="def-content">
                <span><span>the</span> <span>def</span> <span>really</span> <span>1</span></span>
                <div class="def-block def-inline-example">
                    <span class="dbox-example"><span><span>the</span> <span>example</span> <span>1</span></span></span>
                </div>
            </div>
        </div>
        <div class="def-set">
            <span class="def-number">5</span>
            <div class="def-content">
                <span>the def really 2</span>
            </div>
        </div>
    </section>



    <section class="def-pbk">
        <header class="luna-data-header">
            <span class="dbox-pg"><span><span>pos1;</span></span></span><span>, </span><span class="dbox-pg"><span><span>pos2;</span> </span></span><span class="dbox-bold"><span><span>pos3;</span> </span></span><span class="dbox-pg"><span><span>pos4;</span> </span></span><span class="dbox-bold"><span><span>pos5;</span> </span></span>
        </header>
        <div class="def-set">
            <span class="def-number">5</span>
            <div class="def-content">
                <span>the def really 2</span>
            </div>
        </div>
    </section>
        """),
        'result': Word('test', {
            'pos (some kind, of pos)': [
                Definition('the def really 1', 'the example 1'),
                Definition('the def really 2')
            ],
            'pos2': [
                Definition('the def really 1', 'the example 1'),
                Definition('the def really 2')
            ],
            'pos1;, pos2; pos3; pos4; pos5;': [
                Definition('the def really 2')
            ]
        }, None)
    },
    {
        'html': container.format("""
    <div class="def-pbk">
        <span class="dbox-pg"><span><span>pos</span> </span></span><span>(</span><span class="dbox-bold"><span><span>pos1,</span> <span>pos2</span></span></span><span>)</span>
        <div class="def-set">
            <span class="def-number"><span><span>5</span> </span>
            </span>
            <div class="def-content">
                <span><span>the</span> <span>def</span> <span>2</span><span>!</span></span>
            </div>
        </div>
    </div>
        """),
        'result': Word('test', {
            'pos (pos1, pos2)': [
                Definition('the def 2!')
            ]
        }, None)
    }
]
