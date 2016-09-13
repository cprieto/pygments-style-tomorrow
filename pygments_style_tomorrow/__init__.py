# -*- coding: utf-8 -*-
"""
Pygments style for the tomorrow css theme https://github.com/MozMorris/tomorrow-pygments

:copyright: Copyright 2016 Cristian Prieto
:licence: MIT?
"""

from pygments.style import Style
from pygments.token import Comment, Error, Keyword, Literal, Name, Operator, Punctuation, Generic, Text


class TomorrowStyle(Style):
    """
    Tomorrow style for Pygments
    """

    highlight_color = '#d6d6d6'
    background_color = '#fff'
    default_style = 'bg:#fff #4d4d4c'

    styles = {
        Comment: '#8e908c',
        Comment.Multiline: '#8e908c',
        Comment.Preproc: '#8e908c',
        Comment.Single: '#8e908c',
        Comment.Special: '#8e908c',
        Comment.Deleted: '#8e908c',

        Error: '#c82829',
        Operator: '#3e999f',
        Punctuation: '#4d4d4c',

        Generic.Emph: 'italic',
        Generic.Heading: 'bold #4d4d4c',
        Generic.Inserted: '#718c00',
        Generic.Prompt: '#8e908c',
        Generic.Strong: 'bold',
        Generic.Subheading: 'bold #3e999f',

        Keyword: '#8959a8',
        Keyword.Constant: '#8959a8',
        Keyword.Declaration: '#8959a8',
        Keyword.Namespace: '#3e999f',
        Keyword.Pseudo: '#8959a8',
        Keyword.Reserved: '#8959a8',
        Keyword.Type: '#eab700',

        Literal.Date: '#718c00',
        Literal.Number: '#f5871f',
        Literal.String: '#718c00',
        Literal.String.Char: '#4d4d4c',
        Literal.String.Doc: '#8e908c',
        Literal.String.Double: '#718c00',
        Literal.String.Heredoc: '#718c00',
        Literal.String.Escape: '#f5871f',
        Literal.String.Interpol: '#f5871f',

        Name: '#4d4d4c',
        Name.Attribute: '#4271ae',
        Name.Builtin: '#4d4d4c',
        Name.Class: '#eab700',
        Name.Constant: '#c82829',
        Name.Decorator: '#3e999f',
        Name.Entity: '#4d4d4c',
        Name.Exception: '#c82829',
        Name.Function: '#4271ae',
        Name.Label: '#4d4d4c',
        Name.Namespace: '#eab700',
        Name.Other: '#4271ae',
        Name.Property: '#4d4d4c',
        Name.Tag: '#3e999f',
        Name.Variable: '#c82829',

        Text: '#4d4d4c'
    }
