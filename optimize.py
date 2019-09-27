import multiprocessing
import numpy as np

from multiprocessing import Pool

from lib.env.reward import WeightedUnrealizedProfit

np.warnings.filterwarnings('ignore')


def optimize_code(params):
    from lib.RLTrader import RLTrader

    trader = RLTrader(**params)
    trader.optimize()

    return ""


if __name__ == '__main__':
    n_processes = multiprocessing.cpu_count()
    params = {'n_envs': n_processes, 
                'reward_strategy': WeightedUnrealizedProfit,
                "input_data_path": "data/input/base.csv",
                "tensorboard_path": "data/log/tensorboard",
                "cliprange": 0.16054335813960433,
                "ent_coef": 6.467269173440328e-07,
                "gamma": 0.9883526975269143,
                "lam": 0.8108241035751231,
                "learning_rate": 4.2394099015529026e-05,
                "n_steps": 633.7772793108021,
                "noptepochs": 40.793888700955236}

    # opt_pool = Pool(processes=n_processes)
    # results = opt_pool.imap(optimize_code, [params for _ in range(n_processes)])

    # print([result.get() for result in results])

    from lib.RLTrader import RLTrader

    trader = RLTrader(**params)
    trader.train(test_trained_model=True, render_test_env=True, render_report=True, save_report=True)
