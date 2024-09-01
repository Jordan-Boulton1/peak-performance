from django.shortcuts import render

from checkout.models import Order
from .models import TrainingPlan

# Create your views here.


def plans(request):
    """Returns the rendered plans page."""
    plans = TrainingPlan.objects.all()
    # Initialize an empty list for training plan IDs
    user_ordered_plan_ids = []

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Retrieve the training plan IDs from the user's orders
        user_ordered_plan_ids = Order.objects.filter(
            user=request.user).values_list('training_plan_id', flat=True)

    return render(request, "plans/plans.html", {
        'plans': plans,
        # Pass the list of training plan IDs to the template
        'user_ordered_plan_ids': user_ordered_plan_ids,
    })
