var siteApp = angular.module("siteApp",[]);

$(function() {setInterval(function() {
  $("#bodyer").css("height", "auto");
  var vh = $(window).height();
  var hh = $("header").height();
  var bh = $("#bodyer").height();
  var fh = $("footer").height();
  if (vh > hh + bh + fh) $("#bodyer").height(vh - hh - fh);
}, 200);});

siteApp.controller("UserCtrl", ["$scope", "$http", function($scope, $http){
  $scope.list = [{
    id: 1,
    name: "小明",
    gender: "M",
    dob: 563414400,
    avatar: "avatar-1.jpg"
  }, {
    id: 2,
    name: "张晓网",
    gender: "M",
    dob: 663414400,
    avatar: "avatar-2.jpg"
  }];
}]);