import domain
from constants import *
from helper import * 
from point_interpretor import *

if MODE == 5:
    from disjunction_of_intervals_interpretor_loop_importance_sampling import *
    # print('here')
    if DOMAIN == "interval":
        def initialization(x_l, x_r):
            symbol_table_list = list()
            symbol_table = dict()

            symbol_table['h0'] = domain.Interval(x_l[0], x_r[0])
            symbol_table['h1'] = domain.Interval(-x_r[0], -x_l[0])
            symbol_table['v0'] = domain.Interval(0.0, 0.0)
            symbol_table['t_down'] = domain.Interval(0.0, 0.0)
            symbol_table['t_up'] = domain.Interval(0.0, 0.0)

            symbol_table['res'] = domain.Interval(0.0, 0.0)
            symbol_table['x_min'] = domain.Interval(P_INFINITY.data.item(), P_INFINITY.data.item())
            symbol_table['x_max'] = domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())
            symbol_table['x_memo_list'] = list([domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())])
            symbol_table['res_list'] = list()
            symbol_table['probability'] = var(1.0)
            symbol_table['explore_probability'] = var(1.0)

            symbol_table_list.append(symbol_table)

            return symbol_table_list


if MODE == 4:
    from disjunction_of_intervals_interpretor_loop import *

    def initialization(x_l, x_r):

        symbol_table_list = list()

        symbol_table = dict()
        # symbol_table['i'] = domain.Interval(0, 0)
        symbol_table['h0'] = domain.Interval(x_l[0], x_r[0])
        symbol_table['h1'] = domain.Interval(-x_r[0], -x_l[0])
        symbol_table['v0'] = domain.Interval(0.0, 0.0)
        symbol_table['t_down'] = domain.Interval(0.0, 0.0)
        symbol_table['t_up'] = domain.Interval(0.0, 0.0)
        symbol_table['res'] = domain.Interval(0.0, 0.0)
        
        symbol_table['x'] = domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())
        symbol_table['probability'] = var(1.0)

        symbol_table_list.append(symbol_table)
        
        return symbol_table_list

if MODE == 2:
    from disjunction_of_intervals_interpretor import *

    def initialization(x_l, x_r):

        symbol_table_list = list()

        symbol_table = dict()
        # symbol_table['i'] = domain.Interval(0, 0)
        symbol_table['h0'] = domain.Interval(x_l[0], x_r[0])
        symbol_table['h1'] = domain.Interval(-x_r[0], -x_l[0])
        symbol_table['v0'] = domain.Interval(0.0, 0.0)
        symbol_table['t_down'] = domain.Interval(0.0, 0.0)
        symbol_table['t_up'] = domain.Interval(0.0, 0.0)
        symbol_table['res'] = domain.Interval(0.0, 0.0)
        
        symbol_table['x'] = domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())
        symbol_table['probability'] = var(1.0)

        symbol_table_list.append(symbol_table)
        
        return symbol_table_list


if MODE == 3:
    from partial_disjunction_of_intervals_interpretor import *

    def initialization(x_l, x_r):

        symbol_table_list = list()

        symbol_table = dict()
        # symbol_table['i'] = domain.Interval(0, 0)
        symbol_table['h0'] = domain.Interval(x_l[0], x_r[0])
        symbol_table['h1'] = domain.Interval(-x_r[0], -x_l[0])
        symbol_table['v0'] = domain.Interval(0.0, 0.0)
        symbol_table['t_down'] = domain.Interval(0.0, 0.0)
        symbol_table['t_up'] = domain.Interval(0.0, 0.0)
        symbol_table['res'] = domain.Interval(0.0, 0.0)
        
        symbol_table['x'] = domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())
        symbol_table['probability'] = var(1.0)

        symbol_table_list.append(symbol_table)
        
        return symbol_table_list


if MODE == 1:
    from interval_interpretor import *

    def initialization(x_l, x_r):
        
        symbol_table = dict()
        # symbol_table['i'] = domain.Interval(0.0, 0.0)
        symbol_table['h0'] = domain.Interval(x_l[0], x_r[0])
        symbol_table['h1'] = domain.Interval(-x_r[0], -x_l[0])
        symbol_table['v0'] = domain.Interval(0.0, 0.0)
        symbol_table['t_down'] = domain.Interval(0.0, 0.0)
        symbol_table['t_up'] = domain.Interval(0.0, 0.0)
        symbol_table['res'] = domain.Interval(0.0, 0.0)
        
        symbol_table['x'] = domain.Interval(N_INFINITY.data.item(), N_INFINITY.data.item())
        symbol_table['probability'] = var(1.0)
        
        return symbol_table


def initialization_point(x):

    symbol_table = dict()
    # symbol_table['i'] = var(0.0)
    symbol_table['h0'] = var(x[0])
    symbol_table['h1'] = var(-x[0])
    symbol_table['v0'] = var(0.0)
    symbol_table['t_down'] = var(0.0)
    symbol_table['t_up'] = var(0.0)
    symbol_table['res'] = var(0.0)
    
    symbol_table['x_min'] = P_INFINITY
    symbol_table['x_max'] = N_INFINITY
    symbol_table['probability'] = var(1.0)
    symbol_table['explore_probability'] = var(1.0)

    return symbol_table


# function in ifelse condition
def fself(x):
    return x


def f1(x):
    return torch.sqrt(var(2.0).div(var(9.8))).mul(torch.sqrt(x[1]))
def f1_domain(x):
    return x[1].sqrt().mul(torch.sqrt(var(2.0).div(var(9.8))))
def f2(x):
    return (var(0.8).div(var(9.8))).mul(x[1].add(var(9.8).mul(x[2])))
def f2_domain(x):
    return x[1].add(x[2].mul(var(9.8))).mul(var(0.8).div(var(9.8)))
def f3(x):
    return x[0].add(x[1].add(x[2]))
def f3_domain(x):
    return x[0].add(x[1].add(x[2]))
def f4(x):
    return var(4.9).mul(x[1].mul(x[1]))
def f4_domain(x):
    return x[1].mul(x[1]).mul(var(4.9))
def f6(x):
    return var(7.0)
def f6_domain(x):
    return x[0].setValue(var(7.0))
def f7(x):
    return var(0.0)
def f7_domain(x):
    return x[0].setValue(var(0.0))
def f_max(x):
    return torch.max(x[0], x[1])
def f_max_domain(x):
    return x[0].max(x[1])
def f_min(x):
    return torch.min(x[0], x[1])
def f_min_domain(x):
    return x[0].min(x[1])

def f9(x):
    return x[0].add(var(1.0))
def f9_domain(x):
    return x[0].add(var(1.0))
def f_neg(x):
    return x[1].mul(var(-1.0))
def f_neg_domain(x):
    return x[1].mul(var(-1.0))


def construct_syntax_tree(Theta):
    l10 = Assign(['h1', 'h0'], f_neg_domain, None)

    l6 = Assign(['v0'], f6_domain, None)
    l7 = Assign(['v0'], f7_domain, None)
    l9 = Assign(['x_min', 'h0'], f_min_domain, l10)
    l8 = Assign(['x_max', 'h0'], f_max_domain, l9)
    
    l5 = Ifelse('h0', Theta, fself, l6, l7, l8)
    l4 = Assign(['h0', 't_up'], f4_domain, l5)
    l3 = Assign(['res', 't_up', 't_down'], f3_domain, l4)
    l2 = Assign(['t_up', 'v0', 't_down'], f2_domain, l3)

    l1 = Assign(['t_down', 'h0'], f1_domain, l2)
    l1_0 = Assign(['h0', 'h1'], f_neg_domain, l1)
    l0 = WhileSample('h1', var(-4.0), l1_0, None)

    tree_dict = dict()
    tree_dict['entry'] = l0
    tree_dict['para'] = Theta

    return tree_dict


def construct_syntax_tree_point(Theta):

    l10 = AssignPoint(['h1', 'h0'], f_neg, None)

    l6 = AssignPoint(['v0'], f6, None)
    l7 = AssignPoint(['v0'], f7, None)
    
    l9 = AssignPoint(['x_min', 'h0'], f_min, l10)
    l8 = AssignPoint(['x_max', 'h0'], f_max, l9)
    
    l5 = IfelsePoint('h0', Theta, fself, l6, l7, l8)
    l4 = AssignPoint(['h0', 't_up'], f4, l5)
    l3 = AssignPoint(['res', 't_up', 't_down'], f3, l4)
    l2 = AssignPoint(['t_up', 'v0', 't_down'], f2, l3)

    l1 = AssignPoint(['t_down', 'h0'], f1, l2)
    l1_0 = AssignPoint(['h0', 'h1'], f_neg, l1)
    l0 = WhilePoint('h1', var(-4.0), l1_0, None)

    tree_dict = dict()
    tree_dict['entry'] = l0
    tree_dict['para'] = Theta

    return tree_dict


def construct_syntax_tree_smooth_point(Theta):

    l10 = AssignPointSmooth(['h1', 'h0'], f_neg, None)

    l6 = AssignPointSmooth(['v0'], f6, None)
    l7 = AssignPointSmooth(['v0'], f7, None)

    l9 = AssignPointSmooth(['x_min', 'h0'], f_min, l10)
    l8 = AssignPointSmooth(['x_max', 'h0'], f_max, l9)
    
    l5 = IfelsePointSmooth('h0', Theta, fself, l6, l7, l8)
    l4 = AssignPointSmooth(['h0', 't_up'], f4, l5)
    l3 = AssignPointSmooth(['res', 't_up', 't_down'], f3, l4)
    l2 = AssignPointSmooth(['t_up', 'v0', 't_down'], f2, l3)

    l1 = AssignPointSmooth(['t_down', 'h0'], f1, l2)
    l1_0 = AssignPointSmooth(['h0', 'h1'], f_neg, l1)
    l0 = WhilePointSmooth('h1', var(-4.0), l1_0, None)

    tree_dict = dict()
    tree_dict['entry'] = l0
    tree_dict['para'] = Theta

    return tree_dict