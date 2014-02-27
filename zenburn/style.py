'''
    pygments.styles.zenburn
    ~~~~~~~~~~~~~~~~~~~~~~~

    Mimic the Zenburn color scheme: http://slinky.imukuppi.org/zenburnpage/
'''
import pygments.style
import pygments.token


class ZenburnStyle(pygments.style.Style):
    '''Zenburn color scheme.'''

    background_color = '#3f4040'
    highlight_color = '#2f2f2f'
    styles = {
        pygments.token.Text: '#dcdccc',  # ''
        pygments.token.Whitespace: '#000000',  # 'w'
        pygments.token.Error: '#e37170',  # 'err'
        pygments.token.Other: '#000000',  # 'x'
        pygments.token.Comment: '#7f9f7f',  # 'c'
        pygments.token.Punctuation: '#dcdccc',  # 'p'
        pygments.token.Number: '#8cd0d3',  # 'm'
        pygments.token.String: '#cc9393',  # 's'
        pygments.token.Keyword: '#f0dfaf',  # 'k'
        pygments.token.Keyword.Constant: 'bold #dca3a3',  # 'kc'
        pygments.token.Keyword.Namespace: 'bold #dfaf8f',  # 'kn'
        pygments.token.Operator: '#dcdccc',  # 'o'
        pygments.token.Operator.Word: '#f0efd0',  # in not is
        pygments.token.Name: '#dcdccc',  # 'n'
        pygments.token.Name.Builtin: '#efef8f',  # 'nb'
        pygments.token.Name.Builtin.Pseudo: '#efef8f',  # 'bp'
        pygments.token.Name.Class: '#efef8f',  # 'nc'
        pygments.token.Name.Decorator: '#efef8f',  # 'nd'
        pygments.token.Name.Exception: 'bold #ebed9f',  # 'ne'
        pygments.token.Name.Function: '#efef8f',  # 'nf'
        pygments.token.Name.Namespace: '#dcdccc',  # 'nn'
        pygments.token.Name.Variable.Class: '#efef8f',  # 'vc'
    }
