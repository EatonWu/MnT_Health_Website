from django.shortcuts import render
from django.http import HttpResponse
from forms import forms


# The index will prompt users for a number of days
# /dayselector/
def index(request):
    if request.method == "POST":
        form = forms.DayForm(request.POST)

        if form.is_valid():
            # return HttpResponse(form.cleaned_data['day'])
            # instead of returning form data, render the button html file
            if form.cleaned_data['day'] == 1:
                return HttpResponse(
                    "(Option 1) The full body workout is recommended for those who want to increase overall strength and "
                    "don’t have much time in their schedule to workout. This plan consists of a few exercises to "
                    "work each muscle group." + "<br> <br> <b>3-4 sets of 10-12 reps"
                    + "<br> -Barbell Deadlift" + "<br> -Bench Press" + "<br> -Barbell Row" + "<br> -Dumbbell curls" +
                    "<br> -Barbell Back Squats" + "<br> -Rope Pushdowns" + "<br> -Lateral Raises")

            if form.cleaned_data['day'] == 2:
                return HttpResponse(
                    "(Option 1) The full body workout is recommended for those who want to increase overall strength and "
                    "don’t have much time in their schedule to workout. This plan consists of a few exercises to "
                    "work each muscle group.<br> " + "<br> <br> 3-4 sets of 10-12 reps" +  "<br> Full Body Workout: " +
                    "<br> -Barbell Deadlift"+ "<br> -Bench Press" + "<br> -Barbell Row" + "<br> -Dumbbell curls" +
                    "<br> -Barbell Back Squats" + "<br> -Rope Pushdowns" + "<br> -Lateral Raises <br>" +
                    "<br> <br>(Option 2) The Upper Lower Split is a divide and conquer workout split. "
                    "With one day being devoted to the upper body and the other being devoted" +
                    " to lower." + "<br> 3-4 sets of 10-12 reps" + "<br> <br> Upper Body Day:" +
                    "<br> -Bench Press" + "<br> -Bent Over Row"
                    + "<br> -Shoulder Press" + "<br> -Lat Pulldown" + "<br> -Tricep Extenstions"
                    + "<br> -Side Lateral Raises" + "<br> -Pushups" + "<br><br> Lower Body Day:"
                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                    + "<br> Hamstring Curls" + "<br> Lunges")
            if form.cleaned_data['day'] == 3:
                return HttpResponse("(Option 1) This workout plan encompasses multiple muscle groups in the same day. "
                                    "This style works antagonist muscles to ensure that muscles being worked have alternate rest periods."
                                    + "<br> <br> 3-4 sets of 10-12 reps" + "<br> <br> Day 1: Chest + Back + Abs:" +
                                    "<br> Barbell Chest Press " + "<br> Cable Pulldown" + "<br> Barbell Incline Press" + "<br> Barbell Bent Over Row" +
                                    "<br> Pushups" + "<br> V-Bar Cable Row" + "<br> Planks" + "<br> Crunches" + "<br> <br> Day 2: Shoulder + Arms:" +
                                    "<br> Underhand Lat Pulldown" + "<br> Tricep Dips" + "<br> Dumbbell bicep curls" +
                                    "<br> Rope push downs" + "<br> Dumbbell shoulder press" + "<br> Side lateral Raises" +
                                    "<br> <br> Day 3 Legs:" + "<br> Barbell Back Squats" + "<br> Leg Extensions" + "<br> Hip Thrusts" +
                                    "<br> Seated Hamstring Curls" + "<br> Bulgarian Split Squats" + "<br> Calf Raises" +
                                    "<br> <br>(Option 2) The push/pull/legs split is a very simple training method in which you split your"
                                    " body into three parts. And each part is then trained on its own separate day." + "<br> <br>"
                                                                                                                       " 3-4 sets of 10-12 reps" + "<br> <br> Day 1 Push Workout: " + "<br> Seated Dumbbell Shoulder Press"
                                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                                    + "<br> Incline Dumbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br> Day 2 Pull Workout:"
                                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br> Day 3 Leg Workout: " + "<br> Barbell Back Squats"
                                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                                    + "<br> Bulgarian Split Squats")

            if form.cleaned_data['day'] == 4:
                return HttpResponse("(Option 1) The Upper Lower Split is a divide and conquer workout split. "
                                    "With one day being devoted to the upper body and the other being devoted "
                                    "to lower." + "<br> <br> 3-4 sets of 10-12 reps" + "<br> <br>Day 1 Upper Body Day:" + "<br> Bench Press" +
                                    "<br> Bent Over Row"
                                    + "<br> Shoulder Press" + "<br> Lat Pulldown" + "<br> Tricep Extenstions"
                                    + "<br> Side Lateral Raises" + "<br> Pushups" + "<br><br> Day 2 Leg Day:"
                                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                                    + "<br> Hamstring Curls" + "<br> Lunges" + "<br> repeat")
            if form.cleaned_data['day'] == 5:
                return HttpResponse(
                    "(Option 1) Push, Pull, Legs, Upper, Lower This workout split combines push,pull, legs which"
                    "works an entire muscle group on one day allowing for up to 3 days of rest and devoting the"
                    "other two days to your upper/lower body." + "<br> <br>"
                                                                 " 3-4 sets of 10-12 reps" + "<br> <br> Push Workout: " + "<br> Seated Dumbbell Shoulder Press"
                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                    + "<br> Incline Dumbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br> Pull Workout:"
                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br> Leg Workout: " + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                    + "<br> Bulgarian Split Squats" + " to lower." + "<br> 3-4 sets of 10-12 reps" + "<br> <br> Upper Day:"
                                                                                                     "<br> -Bench Press" + "<br> -Bent Over Row"
                    + "<br> -Shoulder Press" + "<br> -Lat Pulldown" + "<br> -Tricep Extenstions"
                    + "<br> -Side Lateral Raises" + "<br> -Pushups" + "<br><br> Lower Day:"
                    + "<br> Front Squats" + "<br> Straight Leg Deadlift" + "<br> Calf Raises" + "<br> Leg Extensions"
                    + "<br> Hamstring Curls" + "<br> Lunges" + "<br> <br>" + "(Option 2) One Muscle A Day: This workout split"
                                                                             " emphasizes a new part of the body each day of working out and allows for optimal rest." + "<br><br> 3-4 Sets of 10-12 Reps"
                    + "<br> <br>Day 1 Chest Day: " + "<br> Bench Press" + "<br> Incline Dumbbell Press" + "<br> Lower Cable Flys"
                    + "<br> Upper Cable Flys" + "<br> Pushups" + "<br><br> Day 2 Leg Day: " + "<br> Barbell Back Squats"
                    + "<br> Seated Leg Extensions" + "<br> Seated Hamstring Curls" + "<br> Calf Raises" + "<br> Bulgarian Split Squats"
                    + "<br> <br> Day 3 Shoulders: " + "<br> Overhead Press" + "<br> Side Lateral Raises" + "<br> Dumbbell Push Press"
                    + "<br> Cable Face Pulls" + "<br><br> Day 4 Back Day:" + "<br> Pullups" + "<br> Barbell Bentover Row"
                    + "<br> Lat Pull Downs" + "<br> Farmer Carries" + "<br> Close grip cable rows" + "<br>"
                    + "<br> Day 5 Arms: " + "<br> Dumbbell Curls" + "<br> Preacher Curls" + "<br> Hammer Curls"
                    + "<br> Rope Pushdowns" + " <br> Tricep Dips" + "<br> Katana Extensions")
            if form.cleaned_data['day'] == 6:
                return HttpResponse("(Option 1) This workout plan encompasses multiple muscle groups in the same day. "
                                    "This style works antagonist muscles to ensure that muscles being worked have alternate rest periods." +
                                    "<br> <br> 3-4 sets of 10-12 reps" + "<br> <br> Day 1: Chest + Back + Abs:" +
                                    "<br> Barbell Chest Press " + "<br> Cable Pulldown" + "<br> Barbell Incline Press" + "<br> Barbell Bent Over Row" +
                                    "<br> Pushups" + "<br> V-Bar Cable Row" + "<br> Planks" + "<br> Crunches" + "<br> <br> Day 2: Shoulder + Arms:" +
                                    "<br> Underhand Lat Pulldown" + "<br> Tricep Dips" + "<br> Dumbbell bicep curls" +
                                    "<br> Rope push downs" + "<br> Dumbbell shoulder press" + "<br> Side lateral Raises" +
                                    "<br> <br> Day 3 Legs:" + "<br> Barbell Back Squats" + "<br> Leg Extensions" + "<br> Hip Thrusts" +
                                    "<br> Seated Hamstring Curls" + "<br> Bulgarian Split Squats" + "<br> Calf Raises" + "<br> <br> Rest and Repeat" +
                                    "<br> <br> (Option 2) The push/pull/legs split is a very simple training method in which you split your"
                                    " body into three parts. And each part is then trained on its own separate day." + "<br> <br>"
                                                                                                                       " 3-4 sets of 10-12 reps" + "<br> <br> Push Workout: " + "<br> Seated Dumbbell Shoulder Press"
                                    + "<br> Dumbbell Incline Press" + "<br> Body Weight Tricep Dips" + "<br> Rope Tricep Pushdowns"
                                    + "<br> Incline Dumbell Fly" + "<br> Dumbbell Lateral Raises" + "<br> <br> Pull Workout:"
                                    + "<br> Bent Over Cable Row" + "<br> Cable Push Down" + "<br> Dumbbell Shrugs" + "<br> Bicep Curls"
                                    + "<br> Hammer Curls" + "<br> Face Pulls" + "<br> <br> Leg Workout: " + "<br> Barbell Back Squats"
                                    + "<br> Seated Leg Extensions" + "<br> Calf Raises" + "<br> Seated Hamstring Curls"
                                    + "<br> Bulgarian Split Squats" + "<br> <br> Rest and Repeat")
    else:
        form = forms.DayForm()

    return render(request, 'day_selector/index.html', {'form': form})

# /day_selector/day
def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")
