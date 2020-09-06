const { spawn } = require('child_process');
const JSONStream = require('JSONStream');

defaults = {
    "sensors": {
		"imu": {
			"angular": {
				"x": 0,
				"y": 0,
				"z": 0
			},
			"accel": {
				"x": 0,
				"y": 0,
				"z": 0
			}
		},
		"depth": 0
	}
}


const sensor = spawn('python3', ['-u', 'sensor.py']);

sensor.stdout.pipe(JSONStream.parse())
    .on('data', data => {
        //console.log(data);
        //defaults.sensors.imu.angular = data.angular;
        //defaults.sensors.imu.accel = data.linear;
        defaults.sensors.depth = data;
        console.log(defaults.sensors.depth);
    });
sensor.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});