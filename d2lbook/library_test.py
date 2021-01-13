from d2lbook import library
import unittest

from collections import namedtuple

class Cell:
    def __init__(self, cell_type, source):
        self.cell_type = cell_type
        self.source = source
class Nb:
    def __init__(self, cells):
        self.cells = cells

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.nb = Nb([Cell('code', '')])
        self.tab_lib = {
            'lib_name':'torch',
            'simple_alias': 'ones, zeros, tensor, arange, meshgrid, sin, sinh, cos, cosh, tanh, linspace, exp, log, normal, rand, matmul, int32, float32, concat -> cat, stack, abs, eye',
            'fluent_alias': 'numpy -> detach().numpy, reshape, size -> numel, to, reduce_sum -> sum, argmax, astype -> type, transpose -> t',
            'alias':'',
            'reverse_alias':'',}

    def test_replace_alias(self):
        # Test https://github.com/d2l-ai/d2l-book/issues/14
        pairs = [ # before, after
            ('X = d2l.reshape(d2l.arange(10,20),(2,3))',
             'X = torch.arange(10,20).reshape((2,3))'),
            ('d2l.numpy(a)', 'a.detach().numpy()'),
            ('d2l.transpose(a)', 'a.t()'),
            ('metric.add(l * d2l.size(y), d2l.size(y))',
             'metric.add(l * y.numel(), y.numel())'),
            ('float(d2l.reduce_sum(cmp.astype(y.dtype)))',
             'float(cmp.astype(y.dtype).sum())'),
            ('d2l.numpy(nn.LeakyReLU(alpha)(x))',
             'nn.LeakyReLU(alpha)(x).detach().numpy()'),
            ('d2l.reshape(X_tile(1 - d2l.eye(n_train)).astype(\'bool\')),',
             'X_tile(1 - torch.eye(n_train)).astype(\'bool\').reshape()'),
            ('float(d2l.reduce_sum(d2l.astype(cmp, y.dtype)))',
             'float(cmp.astype(y.dtype).sum())'),
            # TODO(mli), a bunch of other cases
            # float(d2l.reduce_sum(d2l.abs(Y1 - Y2))) < 1e-6
            # d2l.plt.scatter(d2l.numpy(features[:, 1]), d2l.numpy(labels), 1);
            # d2l.plt.scatter(d2l.numpy(data[:100, 0]), d2l.numpy(data[:100, 1]));
            # d2l.reshape(multistep_preds[i - tau: i], (1, -1)))
            # X = d2l.reshape(d2l.arange(16, dtype=d2l.float32), (1, 1, 4, 4))
            # Y[i, j] = d2l.reduce_sum((X[i: i + h, j: j + w] * K))
            # d2l.reshape(multistep_preds[i - tau: i], (1, -1)))
        ]
        # for a, b in pairs:
            # self.nb.cells[0].source = a
            # nb = library.replace_alias(self.nb, self.tab_lib)
            # self.assertEqual(nb.cells[0].source, b)

