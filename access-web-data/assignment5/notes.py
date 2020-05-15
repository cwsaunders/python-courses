# urllib / API notes:

'''
Wire protocol -- How data is transferred across the network
XML, JSON, etc

    XML (eXtensible Markup Language):

    1. Primary purpose: share structured data
    2. start tag, end tag, text content, attribute, self closing tag
    Example:
    <person>
    <name>chuck</name>
    <phone type='intl'>
    +1 734 303 4456
    </phone>
    <email hide='yes'/>
    </person>
    3. tags can be whatever you want. <ingrediants> , <phone> , <country> , etc
    4. XML as a tree:
    outer document == top node
    inner documents continue to work down the tree.
    extremely similar to HTML, other markup languages
    5. Attributes can change the structure of the tree
    6. XML path: 'draw the tree than walk down the tree'
    /a/b/c/d
    d/e/g
    similar to moving through directories on a computer

    XML Schema:
    screenshots of slides on phone

    '''
