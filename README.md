# padded-resizer
Python Script for Dataset preparation with command line arguments which batch resizes square images to the designated size specified and keeps the ratio of non square images while adding a border to them.

## Command Line arguments: 
```
-src SourceFolderName -des DestinationFolderName -d desiredSize
```
## Example usage: 
```
python padding_resizer.py -src input -des output -d 512
```

