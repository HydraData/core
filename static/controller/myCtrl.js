var app = angular.module('myApp', []);
app.controller('myCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.alerter = function () {
      $http.post('/login', {'user': $scope.user.email, 'pass': $scope.user.password}).then(function () {

      }, function () {

      });
    }
}]);
