# LiDAR-point-cloud-processing

What is LiDAR Point Cloud Processing:

- A point cloud is a discrete set of data points in space. The points may represent a 3D shape or object. Each point position has its set of Cartesian coordinates (X, Y, Z). Point clouds are generally produced by 3D scanners or by photogrammetry software, which measure many points on the external surfaces of objects around them.

- LiDAR stands for light detection and ranging. Aerial LiDAR uses LASER to calculate the distance between the point and the drone (emitting laser) using the same principle as SONAR.

- Each point cloud contains a considerable amount of individual points.

- The two most common tasks in LiDAR point cloud processing is : Semantic and Instance Segmentation

- Semantic Segmentation - Labelling of each point in a general category

- Instance Segmentation - Labelling each point into an object id specifying an individual object within that category

What is DALES:

- DALES object dataset offers a meticulously hand labelled dataset that contains 8 semantic object categories and over 20K hand - labelled instances.

- DALES object presents one of the most extensive segmentation dataset taken with aerial lidar and which provides both urban and rural scenes.

- DALES Object covers over ten square kilometres of aerial lidar with the eight object categories: ground, vegetation, buildings, cars, trucks, powerlines, poles and fences.
- Instance segmentation is provided for all man made objects within the dataset.

Processes:

1) Initial data collection - laser beams are emitted from a high altitude. Due to this considerable distance, the laser pulse diameter can become larger by the time it hits the object. Both relative and absolute errors are taken into account correcting for IMU altitude and positional errors.On average each tile has 12 million points.

2) Preprocessing - This method enables us to find the K nearest neighbours. Upon calculation of the distance of these neighbours from the point of interest, if this distance surpasses the threshold value, we remove this point from the point cloud. This is somewhat a process to filter out some of the points.

3) Semantic and Instance labelling - 
Semantic labelling includes 

Ground: impervious surfaces, grass, rough terrain
Vegetation: trees, shrubs, hedges, bushes
Cars: sedans, vans, SUVs
Trucks: semi-trucks, box-trucks, recreational vehicles
Power lines: transmission and distribution lines
Poles: power line poles, light poles, and transmission towers
Fences: residential fences and highway barriers
Buildings: residential, high-rises and warehouses

We separated each tile into separate layers, with each layer only containing points of the same semantic class. We then performed an initial euclidean clustering on each semantic layer. The pseudo code roughly implements the K-d tree data structure algorithm.


Require:
For each point pi  in the point cloud P ,we calculate k  neighbour
Require: We define an empty list of clusters C, and a queue to be checked, Q
for pi in P do
      Add pi  to Q
      for p  in Q  do
          Get K neighbours for pi
          for pk in K do
              if  pk  not in a cluster then
                  Add pk  to Q
              end if
          end for
      end for
      Label all points in Q as a new cluster in C and clear Q
end for





