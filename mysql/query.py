import subprocess
import pandas as pd
from io import StringIO

def query_db(cmd):
    """Query table in database and return a pandas dataframe

    Parameters
    ----------
    cmd : str
        SQL select statement 

    Returns
    -------
    pd.DataFrame
        Retrieved data in pandas dataframe
    """
    p = subprocess.run(f"mysql -e \"{cmd}\"", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return  pd.read_csv(StringIO(p.stdout.decode()), sep='\t')
