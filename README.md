## Closest Robot Service
This microservice calculates which robot should transport a pallet (or load) from point A to point B
based on which robot is the closest and has the most battery left (if there are multiple in
the proximity of the load's location). This service uses an underlying
[REST](https://www.w3.org/2001/sw/wiki/REST) endpoint in order to help create a simplified robot routing REST service.

This endpoint accepts a `POST`-ed payload that contains a load entity which needs to be moved,
including its identifier and its current cartesian coordinates. This endpoint then returns the robot that is best to transport the load based on which one is closest to the load's location.
However, if there is more than one robot within 10 distance units of the load, this service returns
the robot with the most battery remaining.

#### How to Use:
The REST endpoint is available at `http://localhost:5000/api/robots/closest` once the service is
started.

When JSON data containing a Load's ID, its X Coordinate, and its Y Coordinate,
such as the following is `POST`-ed to the endpoint...
```
{
    "loadId": 100,
    "x": 20,
    "y": 30
}
```

...it will return the closest calculated (considering 10 distance units window and max battery level)
Robot JSON data. This data, as seen below, contains a Robot's ID, its Battery Level, and its Distance
to the Load Goal.
```
{
    "robotId": 34,
    "batteryLevel": 92,
    "distanceToGoal": 5.0
}
```

#### How to Run:
In order to run this service, written using [python3](https://www.python.org), `python3` must
first be present on the system. If not, it needs to be installed.

Once the `python3` environment is setup, a terminal should be used to install the dependencies using
`pip3` and run the service using `python3`:
- Navigate to the root directory of this repository
- Run the following command to install dependencies:
  - `pip3 install -r requirements.txt`
  - Note that `pip3` may need to be replaced with the path for your copy of `pip`
- Next, navigate to the `src` subdirectory
- Then run the service using `python`:
  - `python3 closest_robot_service.py`
  - Note that `python3` may need to be replaced with the path for your copy of `python`

#### How to Test:
Tests demonstrating the aspects of the full usage of the service are available at
`src/test_acceptance_closest_robot_service.py` and `src/test_acceptance_calculators.py`.
These are the best resources to view to understand how the system performs (at a higher level).

All automated tests can be run by navigating to the root of this repository and then
by running the `run_all_tests.sh` script or the command `python3 -m unittest discover -s src`.

For manual testing / a demonstration of how the system can be used using an external tool,
navigate to the directory `manual_json_curl_test` and run the `run_curl_manual_test.sh` script.
Alternatively, you can run the command:
`curl -X POST -H "Content-Type: application/json" -d @test_json_for_curl.json http://localhost:5000/api/robots/closest`.
Note that the service must be running when these commands are executed.
Request / Load data can be changed by editing the contents of the `test_json_for_curl.json` file.

#### To Do / Future Improvements:
Since the time to work on this programming challenge / project was greatly limited (on the scale of
hours and not days), there are several open areas of concern and several improvements that can be made.
These include:
- Documentation:
  - `pydoc` or `Doxygen` comments should be added to the publicly accessible methods, functions, and classes of this
    project to explain what the preconditions, postconditions, accepted data types, returned data types, thrown
    exceptions, etc. are. Currently, the test harness does a reasonable job of explaining how to use the current system and develop a larger system with 
the implementatipon provided in this project, but formal documentation should be provided.
  - High Level, User Documentation could be created to provide a more formal explanation of how this service should be
    employed, depending on its use cases.
- Python Package Setup:
  - More organization to divide and organize the python files / modules into their own directories using the creation of
    `__init__.py` files would allow for more manageable maintenance and future development of this project. Currently,
    there are several files all in one `src` directory. Additionally, the `test_*.py` files could be moved into their
    own corresponding `test` modules. Separating the tests and the implementation can prevent an overwhelming growth of
    files that run the risk of becoming unmanageable.
  - More formal Python Package Setup using the appropriate metadata files such as a `pyproject.toml` file can be more
    beneficial / helpful for the user during the installation process. Being able to install and manage this project
    as a python package can be more efficient from a maintenance perspective vs. manually managing the files (copy /
    paste / delete).
- Additional Test Coverage and Error Handling:
  - There are small, but important holes in the acceptance and integration tests that should be expanded in order to
    cover cases where the network is unavailable or the underlying Robot Data REST Endpoint is unavailble /
    malfunctioning. In order to do this, more complex test fixtures or additional services in a DevOps pipeline would
    need to be created or stood up to help simulate and test these conditions. Furthermore, adding more configurability
    to the main service setup itself could allow for more test coverage since other REST Endpoints could be specified
    at the main entrypoint of the system and allow for the testing of the entire system during an underlying failure or using fake data.
  - Error Handling should be expanded for the main entrypoint of the service; the server code itself likely has room
    for error handling using `try / except` blocks as well as underlying JSON data retrieval through the underlying REST
    service for Robot Data (as mentioned above). Logging to a log file during failures would also be beneficial to
    the developers and the maintainers of the service as part of future debugging and deployment needs.
  - Support for redundancy / backup options for connecting to underlying REST Endpoints would also be a plus in case
    if the main endpoint is unavailable. A reliable service should be able to handle when underlying services are
    unavailable and then attempt to fallback to alternate, redundnant, or backup options. For example, a secondary
    Robot Data REST Endpoint could be connected to in the event that the first is unavailable so that the main service
    still serves as a viable option.
- Production Support:
  - Ideally, a robust, production-ready service should be implemented using a production server instead of one that is
    used for local debuggging and testing. The underlying [Flask](https://flask.palletsprojects.com/en/2.2.x) server
    is only configured currently for debugging. A Web Server Gateway Interface (WSGI) such as `Gunicorn` should be used.
  - Additionally, such a service should be able to support encrypted connections using the `HTTPS` protocol rather than
    plain `HTTP` for the purposes of security, privacy, and data integrity. Some WSGI servers should be able to support
    this. Otherwise, a reverse proxy in front of the WSGI server should be employed such as `nginx`.
- Refactoring:
  - Some of the higher level methods used in the implementation of this project are rather lengthy and complex for a single method.
  - Reducing methods and functions of a larger size into smaller methods and functions reduces maintenance challenges and complexity.
  - Additionally, smaller methods and functions are easier to test and easier to document and read.
- Peer Review:
  - Code Reviews are always important.
  - A second pair of eyes can be the difference between success and failure.
  - Mistakes or misunderstandings in requirements can slip though the cracks, but can be caught and fixed with just a simple review by a peer.

#### Developers / Maintainers:
- William R. Drumheller
