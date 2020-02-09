import sys
sys.path.append('..')
from framework_def import framework


def before_all(Context):
    Context.Framework = framework()

def after_all(Context):
    Context.Framework.TearDown()