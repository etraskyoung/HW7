import scipy.stats as stat
import SurvivalModelClasses as Cls

#Using a mortality probability of .1 to see what the answer would be in this test case

SIM_POP_SIZE = 1000  # population size of simulated cohorts
TIME_STEPS = 1000  # length of simulation
ALPHA = 0.05  # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500  # number of simulated cohorts used to calculate prediction intervals
MORTALITY_PROB = .1

multiCohort = Cls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[SIM_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

print(multiCohort.get_overall_percentage_alive_after_5_years())
