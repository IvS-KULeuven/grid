
import sys, os, glob
import logging
import numpy as np 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class insertion:
  """
  Inserting data into the database tables
  """
  def __init__(self,
               table,
               ):
    """
    class constructor 

    @param table: (default=None); insert data into one of the tables defined in the schema of the 
           database (grid.sql). The allowed values are:
           - tracks
           - models
           - rotation_rates
           - mode_types
           - modes
    @type table: string
    """
    if table not in ['tracks', 'models', 'rotation_rates', 'mode_types', 'modes']:
      logging.error('Error: insert_def: init: requested table not supported')

    self.table = table 

  def set_table(self, table):
    self.table = table 

  def get_table(self):
    return self.table



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
