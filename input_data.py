
from paraview.simple import *
from paraview import coprocessing


#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# ParaView 5.4.1 64 bits

#--------------------------------------------------------------
# Global screenshot output options
imageFileNamePadding=4
rescale_lookuptable=False


# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.4.1

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [970, 747]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.OrientationAxesVisibility = 0
      renderView1.CenterOfRotation = [1046.6950988769531, 1034.859914779663, 0.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [1046.6950988769531, 1034.859914779663, 4038.5608528888934]
      renderView1.CameraFocalPoint = [1046.6950988769531, 1034.859914779663, -1153.1576624465647]
      renderView1.CameraParallelScale = 1343.7156285802002
      renderView1.Background = [0.9333333333333333, 0.9333333333333333, 0.9254901960784314]

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_%t.png', freq=1, fittoscreen=0, magnification=1, width=970, height=747, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'PVD Reader'
      # create a producer from a simulation input
      meshpvd = coprocessor.CreateProducer(datadescription, 'mesh')

      # create a new 'Cell Data to Point Data'
      cellDatatoPointData1 = CellDatatoPointData(Input=meshpvd)

      # create a new 'Contour'
      contour1 = Contour(Input=cellDatatoPointData1)
      contour1.ContourBy = ['POINTS', 'data']
      contour1.Isosurfaces = [1.0]
      contour1.PointMergeMethod = 'Uniform Binning'

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get color transfer function/color map for 'data'
      dataLUT = GetColorTransferFunction('data')
      dataLUT.RGBPoints = [-0.7484961748123169, 0.278431372549, 0.278431372549, 0.858823529412, -0.2018636919260023, 0.0, 0.0, 0.360784313725, 0.3409461861848828, 0.0, 1.0, 1.0, 0.8914012738466259, 0.0, 0.501960784314, 0.0, 1.4342111519575114, 1.0, 1.0, 0.0, 1.980843634843826, 1.0, 0.380392156863, 0.0, 2.5274761177301412, 0.419607843137, 0.0, 0.0, 3.074108600616455, 0.878431372549, 0.301960784314, 0.301960784314]
      dataLUT.ColorSpace = 'RGB'
      dataLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'data'
      dataPWF = GetOpacityTransferFunction('data')
      dataPWF.Points = [-0.7484961748123169, 0.0, 0.5, 0.0, 3.074108600616455, 1.0, 0.5, 0.0]
      dataPWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from meshpvd
      meshpvdDisplay = Show(meshpvd, renderView1)
      # trace defaults for the display properties.
      meshpvdDisplay.Representation = 'Surface'
      meshpvdDisplay.ColorArrayName = ['CELLS', 'data']
      meshpvdDisplay.LookupTable = dataLUT
      meshpvdDisplay.OSPRayScaleArray = 'data'
      meshpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      meshpvdDisplay.SelectOrientationVectors = 'None'
      meshpvdDisplay.ScaleFactor = 204.8
      meshpvdDisplay.SelectScaleArray = 'data'
      meshpvdDisplay.GlyphType = 'Arrow'
      meshpvdDisplay.GlyphTableIndexArray = 'data'
      meshpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
      meshpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
      meshpvdDisplay.GaussianRadius = 102.4
      meshpvdDisplay.SetScaleArray = [None, '']
      meshpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      meshpvdDisplay.OpacityArray = [None, '']
      meshpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'

      # show color legend
      meshpvdDisplay.SetScalarBarVisibility(renderView1, True)

      # show data from contour1
      contour1Display = Show(contour1, renderView1)
      # trace defaults for the display properties.
      contour1Display.Representation = 'Points'
      contour1Display.AmbientColor = [0.0, 0.0, 0.0]
      contour1Display.ColorArrayName = ['POINTS', '']
      contour1Display.PointSize = 3.0
      contour1Display.LineWidth = 4.0
      contour1Display.OSPRayScaleArray = 'Normals'
      contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      contour1Display.SelectOrientationVectors = 'None'
      contour1Display.ScaleFactor = 194.40570259094238
      contour1Display.SelectScaleArray = 'None'
      contour1Display.GlyphType = 'Arrow'
      contour1Display.GlyphTableIndexArray = 'None'
      contour1Display.DataAxesGrid = 'GridAxesRepresentation'
      contour1Display.PolarAxes = 'PolarAxesRepresentation'
      contour1Display.GaussianRadius = 97.20285129547119
      contour1Display.SetScaleArray = [None, '']
      contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
      contour1Display.OpacityArray = [None, '']
      contour1Display.OpacityTransferFunction = 'PiecewiseFunction'

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for dataLUT in view renderView1
      dataLUTColorBar = GetScalarBar(dataLUT, renderView1)
      dataLUTColorBar.AutoOrient = 0
      dataLUTColorBar.WindowLocation = 'AnyLocation'
      dataLUTColorBar.Position = [0.8582989690721647, 0.021532797858099695]
      dataLUTColorBar.Title = ''
      dataLUTColorBar.ComponentTitle = ''
      dataLUTColorBar.TitleBold = 1
      dataLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      dataLUTColorBar.LabelBold = 1
      dataLUTColorBar.LabelShadow = 1
      dataLUTColorBar.LabelFontSize = 20
      dataLUTColorBar.AutomaticLabelFormat = 0
      dataLUTColorBar.LabelFormat = '%-# 6.02f'
      dataLUTColorBar.AddRangeLabels = 0
      dataLUTColorBar.RangeLabelFormat = '%-#6.1f'
      dataLUTColorBar.ScalarBarThickness = 24
      dataLUTColorBar.ScalarBarLength = 0.9475

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(meshpvd)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'mesh': [1, 1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(False, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor
    if datadescription.GetForceOutput() == True:
        # We are just going to request all fields and meshes from the simulation
        # code/adaptor.
        for i in range(datadescription.GetNumberOfInputDescriptions()):
            datadescription.GetInputDescription(i).AllFieldsOn()
            datadescription.GetInputDescription(i).GenerateMeshOn()
        return

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
