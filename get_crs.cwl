cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: eforoutan/get_crs:latest
  NetworkAccess:
    networkAccess: true

inputs:
  input_shapefile:
    type:
      - File
      - Directory
    inputBinding:
      position: 1

outputs:
  output_csv:
    type: File  
    outputBinding:
      glob: "crs_info.csv"