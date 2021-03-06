# Export the Haines data as Geotiffs
#
# Run in the Arc python terminal, opened within the Arcmap containing all the Haines et al 2017 data.
# open the MPK file and run the code below is the easiest way to do this I think
#
# Theodore Barnhart | tbarnhart@usgs.gov | USGS WY-MT WSC | Created: 20170810
############################################################################################
import numpy as np
cellsize = "5280" # 1 mile grid
outdir = "haines_exports_Jan_2018"
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Treatments\sir2017_ActiveModel_Fishnet_join_trtm_totals_1980"
for year in np.arange(1980,2018):
	print 'Starting Year: %s'%(year)
	# Well counts
	arcpy.PolygonToRaster_conversion(in_features="ActiveModel_1mi_Fishnet_Join_WB_TrtmTotal_%s"%(year),
	 value_field="Count_", out_rasterdataset="C:/Users/tbarnhart/projects/UOG/data/%s/well_count%s.tif"%(outdir,year),
	  cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=cellsize)
	print 'Well Count Complete'

	# Frac Water Use
	key = 'Sum_SUMOFTRTM_'
	arcpy.PolygonToRaster_conversion(in_features="ActiveModel_1mi_Fishnet_Join_WB_TrtmTotal_%s"%(year),
	 value_field=key, out_rasterdataset="C:/Users/tbarnhart/projects/UOG/data/%s/treatment_water_%s.tif"%(outdir,year),
	  cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=cellsize)
	print 'Treatment Water Complete'

	# Oil Production by year
	key = 'Sum_X%s'%(str(year)[1:]) # generate the correct key
	arcpy.PolygonToRaster_conversion(in_features="ActiveModel_Join_Oil_Production",
	 value_field=key, out_rasterdataset="C:/Users/tbarnhart/projects/UOG/data/%s/oil_production_%s.tif"%(outdir,year),
	  cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=cellsize)
	print 'Oil Production Complete'

	# Gas Production by year
	arcpy.PolygonToRaster_conversion(in_features="ActiveModel_Join_Gas_Production",
	 value_field=key, out_rasterdataset="C:/Users/tbarnhart/projects/UOG/data/%s/gas_production_%s.tif"%(outdir,year),
	  cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=cellsize)
	print 'Gas Production Complete'

	# Water Production by year
	arcpy.PolygonToRaster_conversion(in_features="ActiveModel_Join_Water_Production",
	 value_field=key, out_rasterdataset="C:/Users/tbarnhart/projects/UOG/data/%s/water_production_%s.tif"%(outdir,year),
	  cell_assignment="CELL_CENTER", priority_field="NONE", cellsize=cellsize)
	print 'Water Production Complete'
	print '*****************************************'

# other functions
	def changeNull(col):
    ```
    Function to write a 1 when a column is Null and a 0 when the column has a value.
    col = column to run the function on
    ```
    if col == None:
        return 1
    else:
        return 0