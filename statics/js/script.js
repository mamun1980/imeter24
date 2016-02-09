'use strict';

var premierApp = angular.module("premierApp", ['ngRoute'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
});



premierApp.filter('googleSearchFilter', function(){
    return function(items, token) {
        
        if(token != undefined && token != "") {
            var output=[];
            var filter_output = [];
            output = items;
            // console.log(output);
            
            var searchArr = token.split(" ");

            for(var j=0; j<searchArr.length; j++) {

                for(var i=0; i<output.length; i++) {
                    // console.log(output[i]);
                    var search_str = output[i].search_string;
                    // We can remove this if statement when all is updated.
                    // console.log(search_str);
                    if (search_str != null) {
                        var n = search_str.search(new RegExp(searchArr[j], "i"));    
                        // console.log('search_str is not null');
                    }
                    // console.log(n);
                    if(n != -1) {
                        filter_output.push(output[i]);
                    }

                }
                output = filter_output;
                filter_output = [];  
            }
            
            return output;

        } else {
            return items;
        }   
    }
});

premierApp.factory("ContactService", function($http, $q){
    var factory = {};

    factory.getAllContacts = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/contacts/list/"}).
            success(function(data, status, headers, config) {
                console.log(data);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});

premierApp.factory("JobService", function($http, $q){
    var factory = {};

    factory.getAllJobs = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/schedule/all-jobs/"}).
            success(function(data, status, headers, config) {
                // console.log(test);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    factory.getCurrentJobs = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/schedule/current-jobs/"}).
            success(function(data, status, headers, config) {
                // console.log(test);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    factory.getMyJobs = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/schedule/my-jobs/"}).
            success(function(data, status, headers, config) {
                // console.log(test);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});

premierApp.factory("EventService", function($http, $q){
    var factory = {};

    factory.getAllEvents = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/events/list/"}).
            success(function(data, status, headers, config) {
                // console.log(test);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };
    factory.getAllControllers = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/events/controller-list/"}).
            success(function(data, status, headers, config) {
                // console.log(test);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});



premierApp.factory("EventEntryService", function($http, $q){
    var factory = {};

    factory.getEntries = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/events/event-entry-list"}).
            success(function(data, status, headers, config) {
                
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});


premierApp.factory("InventoryService", function($http, $q){
    var factory = {};

    factory.getAllItems = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/inventory/items/"}).
            success(function(data, status, headers, config) {
                console.log(data);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});

premierApp.factory("UserService", function($http, $q){
    var factory = {};

    factory.getAllUsers = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/userlist"}).
            success(function(data, status, headers, config) {
                
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});

premierApp.factory("ReportService", function($http, $q){
    var factory = {};

    factory.getAllReports = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/report/job-list"}).
            success(function(data, status, headers, config) {
                // console.log(data);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    factory.getAllJobs = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/report/recuring-job-list"}).
            success(function(data, status, headers, config) {
                console.log(data);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;

    };

    factory.getCurrentJobs = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/report/single-job-list"}).
            success(function(data, status, headers, config) {
                console.log(data);
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;

    };

    return factory;
});


premierApp.factory("MassMailService", function($http, $q){
    var factory = {};

    factory.getMassMails = function() {
        var defer = $q.defer();

        $http({method: 'GET', url: "/get-mass-mails"}).
            success(function(data, status, headers, config) {
                
                defer.resolve(data);
            }).
            error(function(data, status, headers, config) {

            });

        return defer.promise;
    };

    return factory;
});


premierApp.config(function ($routeProvider) {
    $routeProvider
        .when("/contacts", {
            templateUrl: "/statics/js/contacts/contact-list.html",
            controller: "ContactController",
        })
        .when("/schedule/all-jobs", {
            templateUrl: "/statics/js/schedule/all-jobs.html",
            controller: "ScheduleController",
            resolve: {
                jobs: function (JobService) {
                    var alljobs = JobService.getAllJobs();

                    return alljobs;
                }
            }
        })
        .when("/schedule/current-jobs", {
            templateUrl: "/statics/js/schedule/all-jobs.html",
            controller: "ScheduleController",
            resolve: {
                jobs: function (JobService) {
                    var jobs = JobService.getCurrentJobs();

                    return jobs;
                }
            }
        })
        .when("/schedule/my-jobs", {
            templateUrl: "/statics/js/schedule/all-jobs.html",
            controller: "ScheduleController",
            resolve: {
                jobs: function (JobService) {
                    var jobs = JobService.getMyJobs();

                    return jobs;
                }
            }
        })
        // .when("/report/job-list", {
        //     templateUrl: "/statics/js/report/report-job-list.html",
        //     controller: "ReportController",
        //     resolve: {
        //         reports: function (ReportService) {
        //             var reports = ReportService.getAllReports();

        //             return reports;
        //         }
        //     }
        // })
        .when("/report/recuring-job-list", {
            templateUrl: "/statics/js/report/recuring-job-list.html",
            controller: "ReportController",
            resolve: {
                jobs: function (ReportService) {
                    var jobs = ReportService.getAllJobs();

                    return jobs;
                }
            }
        })
        .when("/report/single-job-list", {
            templateUrl: "/statics/js/report/single-job-list.html",
            controller: "ReportController",
            resolve: {
                jobs: function (ReportService) {
                    var jobs = ReportService.getCurrentJobs();

                    return jobs;
                }
            }
        })
        .when("/events/list", {
            templateUrl: "/statics/js/events/list-events.html",
            controller: "EventController",
            resolve: {
                events: function (EventService) {
                    var events = EventService.getAllEvents();

                    return events;
                }
            }
        })
        .when("/events/controller-list", {
            templateUrl: "/statics/js/events/controller-list.html",
            controller: "EventController",
            resolve: {
                controllers: function (EventService) {
                    var controllers = EventService.getAllControllers();

                    return controllers;
                }
            }
            
        })
        .when("/inventory/items", {
            templateUrl: "/statics/js/inventory/inventory-list.html",
            controller: "InventoryController",
            resolve: {
                items: function (InventoryService) {
                    var items = InventoryService.getAllItems();
                    
                    return items;
                }
            }
            
        })
        .when("/userlist", {
            templateUrl: "/statics/js/scomuser/user-list.html",
            controller: "UserController",
            resolve: {
                users: function (UserService) {
                    var users = UserService.getAllUsers();
                    
                    return users;
                }
            }
            
        })
        .when("/events/event-entry-list", {
            templateUrl: "/statics/js/events/event-entry-list.html",
            controller: "EventEntryController",
            resolve: {
                entries: function (EventEntryService) {
                    var entries = EventEntryService.getEntries();
                    
                    return entries;
                }
            }
            
        })
        .when("/get-mass-mails", {
            templateUrl: "/statics/js/utility/mass-mail-list.html",
            controller: "MassMailController",
            resolve: {
                massmails: function (MassMailService) {
                    var massmails = MassMailService.getMassMails();
                    
                    return massmails;
                }
            }
            
        })
        .otherwise({
            redirectTo: '/'
        })
})
