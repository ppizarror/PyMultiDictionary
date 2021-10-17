"""
PyMultiDictionary
https://github.com/ppizarror/PyMultiDictionary

TOKENIZER
Implements a tokenizer from nltk library.
"""

__all__ = ['RegexpTokenizer']

from abc import ABC, abstractmethod
import re
import types


# noinspection PyMissingOrEmptyDocstring
def overridden(method):
    if isinstance(method, types.MethodType) and method.__self__.__class__ is not None:
        name = method.__name__
        funcs = [
            cls.__dict__[name]
            for cls in _mro(method.__self__.__class__)
            if name in cls.__dict__
        ]
        return len(funcs) > 1
    else:
        raise TypeError('Expected an instance method.')


def _mro(cls):
    if isinstance(cls, type):
        return cls.__mro__
    else:
        mro = [cls]
        for base in cls.__bases__:
            mro.extend(_mro(base))
        return mro


# noinspection PyShadowingBuiltins,PyMissingOrEmptyDocstring
def regexp_span_tokenize(s, regexp):
    left = 0
    for m in re.finditer(regexp, s):
        right, next = m.span()
        if right != left:
            yield left, right
        left = next
    yield left, len(s)


# noinspection PyTypeChecker
class TokenizerI(ABC):
    """
    A processing interface for tokenizing a string.
    Subclasses must define ``tokenize()`` or ``tokenize_sents()`` (or both).
    """

    @abstractmethod
    def tokenize(self, s):
        """
        Return a tokenized copy of *s*.

        :rtype: list of str
        """
        if overridden(self.tokenize_sents):
            return self.tokenize_sents([s])[0]

    def span_tokenize(self, s):
        """
        Identify the tokens using integer offsets ``(start_i, end_i)``,
        where ``s[start_i:end_i]`` is the corresponding token.

        :rtype: iter(tuple(int, int))
        """
        raise NotImplementedError()

    def tokenize_sents(self, strings):
        """
        Apply ``self.tokenize()`` to each element of ``strings``.  I.e.:

            return [self.tokenize(s) for s in strings]

        :rtype: list(list(str))
        """
        return [self.tokenize(s) for s in strings]

    def span_tokenize_sents(self, strings):
        """
        Apply ``self.span_tokenize()`` to each element of ``strings``.  I.e.:

            return [self.span_tokenize(s) for s in strings]

        :rtype: iter(list(tuple(int, int)))
        """
        for s in strings:
            yield list(self.span_tokenize(s))


# noinspection PyMissingOrEmptyDocstring
class RegexpTokenizer(TokenizerI):
    r"""
    A tokenizer that splits a string using a regular expression, which
    matches either the tokens or the separators between tokens.

        >>> tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')

    :type pattern: str
    :param pattern: The pattern used to build this tokenizer.
        (This pattern must not contain capturing parentheses;
        Use non-capturing parentheses, e.g. (?:...), instead)
    :type gaps: bool
    :param gaps: True if this tokenizer's pattern should be used
        to find separators between tokens; False if this
        tokenizer's pattern should be used to find the tokens
        themselves.
    :type discard_empty: bool
    :param discard_empty: True if any empty tokens `''`
        generated by the tokenizer should be discarded.  Empty
        tokens can only be generated if `_gaps == True`.
    :type flags: int
    :param flags: The regexp flags used to compile this
        tokenizer's pattern.  By default, the following flags are
        used: `re.UNICODE | re.MULTILINE | re.DOTALL`.

    """

    def __init__(
            self,
            pattern,
            gaps=False,
            discard_empty=True,
            flags=re.UNICODE | re.MULTILINE | re.DOTALL,
    ):
        # If they gave us a regexp object, extract the pattern.
        pattern = getattr(pattern, "pattern", pattern)

        self._pattern = pattern
        self._gaps = gaps
        self._discard_empty = discard_empty
        self._flags = flags
        self._regexp = None

    def _check_regexp(self):
        if self._regexp is None:
            self._regexp = re.compile(self._pattern, self._flags)

    def tokenize(self, text):
        self._check_regexp()
        # If our regexp matches gaps, use re.split:
        if self._gaps:
            if self._discard_empty:
                return [tok for tok in self._regexp.split(text) if tok]
            else:
                return self._regexp.split(text)

        # If our regexp matches tokens, use re.findall:
        else:
            return self._regexp.findall(text)

    def span_tokenize(self, text):
        self._check_regexp()

        if self._gaps:
            for left, right in regexp_span_tokenize(text, self._regexp):
                if not (self._discard_empty and left == right):
                    yield left, right
        else:
            for m in re.finditer(self._regexp, text):
                yield m.span()

    def __repr__(self):
        return "{}(pattern={!r}, gaps={!r}, discard_empty={!r}, flags={!r})".format(
            self.__class__.__name__,
            self._pattern,
            self._gaps,
            self._discard_empty,
            self._flags,
        )
