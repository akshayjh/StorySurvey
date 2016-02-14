var $container = $('.js-story-event-list');
var form = new Form($container);

// Add a new event row to the form for the user to edit
form.addEvent();

// Add a new event row when the `Add event` button is clicked
$('.js-add-event').click(function () {
    form.addEvent();
});

// Save the data that has been added to the form
$('.js-submit-story').click(function () {
    var data = form.getData();

    // For now, just log the data to the console to show that this works
    console.log(data); 
});
