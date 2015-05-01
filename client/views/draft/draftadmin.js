Template.draftadmin.events({
  'click .undo-bid' : function(event) {
    console.log("Removing last bid")
    Meteor.call("removeLastBid", Meteor.user().username);
  },
  'click .pause-auction' : function(event) {
    console.log("Pausing auction")
    Meteor.call("pauseAuction", Meteor.user().username);
  },
  'click .resume-auction' : function(event) {
    console.log("Resuming auction")
    Meteor.call("resumeAuction", Meteor.user().username);
  },
  'click .start-auction' : function(event) {
    console.log("Start auction")
    Meteor.call("startAuction", Meteor.user().username);
  },
  'click .undo-nomination' : function(event) {
    Meteor.call("undoNomination", Meteor.user().username);
  },
  'submit .add-nomination' : function(event) {
    var name = event.target.player.value;
    Meteor.call("toggleState", name, 0);
    return false;
  },
  'submit .set-bidtime' : function(event) {
    bidTime = parseInt(event.target.bidtime.value)*1000;
    Meteor.call('setBidTime', bidTime);
    return false;
  },
})

Template.draftadmin.helpers({
  draftadmin : function() {
    if(Meteor.user() !== undefined) {

      if(draftadmins.indexOf(Meteor.user().username) >= 0) {
        return true;
      }
    }
    return false;
  },
});
