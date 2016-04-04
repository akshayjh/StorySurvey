function Form ($container) {
    this.$container = $container;
    this.events = [];
}

/*
 * Function to return the text of each event in the story.
 */
Form.prototype.getData = function () {
    var data = [];

    for (var i = 0; i < this.events.length; i++) {
        data.push(this.events[i].val());
    }

    return data;
};

/*
 * Function to add an event field to the form.
 */
Form.prototype.addEvent = function () {
    var $row = $('<li class="list-group-item"></li>');
    var $textarea = $('<textarea class="form-control"></textarea>');

    $row.html($textarea);
    this.$container.append($row);

    this.events.push($textarea);
};
