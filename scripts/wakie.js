// Description
//   Wakie Wakie - Pings a random person in #general and asks what they are up to
//

var HubotCron = require('hubot-cronjob');

module.exports = function(robot) {
	var fn, pattern, timezone;
	pattern = '0 17 * * *'; // Daily at 5:00PM
	timezone = 'Australia/Brisbane';

	fn = function() {
		var general = robot.adapter.client.dataStore.getChannelByName("general");
		var active = general.members.filter(function(user) { return robot.brain.userForId(user).-deleted === false; }); // Filter out deleted accounts
		var victim = active[Math.floor(Math.random() * active.length)];
		return robot.messageRoom("general", "Hey <@" + victim + ">! Tell us about something cool you are working on!");
	};
	return new HubotCron(pattern, timezone, fn);
};
