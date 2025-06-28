import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.set_aspect('equal')

# Remove axes
ax.axis('off')

# Title
ax.text(8, 11.5, 'Booking Management System - Use Case Diagram', 
        fontsize=16, fontweight='bold', ha='center')

# System boundary
system_boundary = FancyBboxPatch((1, 1), 14, 10, 
                                boxstyle="round,pad=0.1", 
                                facecolor='lightblue', 
                                edgecolor='black', 
                                linewidth=2, 
                                linestyle='--')
ax.add_patch(system_boundary)
ax.text(8, 10.8, 'Booking Management System', fontsize=14, fontweight='bold', ha='center')

# Actors (stick figures)
actors = [
    ('Customer', 0.5, 8, 'left'),
    ('Administrator', 15.5, 8, 'right'),
    ('Payment Gateway', 0.5, 4, 'left'),
    ('Email System', 15.5, 4, 'right')
]

for name, x, y, align in actors:
    # Stick figure
    ax.plot([x, x], [y-0.5, y+0.5], 'k-', linewidth=3)  # Body
    ax.plot([x-0.3, x+0.3], [y+0.5, y+0.5], 'k-', linewidth=3)  # Arms
    ax.plot([x-0.2, x+0.2], [y-0.5, y-0.8], 'k-', linewidth=3)  # Legs
    circle = plt.Circle((x, y+0.8), 0.3, fill=False, linewidth=3)  # Head
    ax.add_patch(circle)
    
    # Actor name
    if align == 'left':
        ax.text(x-0.5, y, name, fontsize=10, ha='right', va='center', fontweight='bold')
    else:
        ax.text(x+0.5, y, name, fontsize=10, ha='left', va='center', fontweight='bold')

# Use Cases (ovals)
use_cases_customer = [
    'Register Account', 'Login/Logout', 'Search Services', 'Make Booking',
    'Modify Booking', 'Cancel Booking', 'Make Payment', 'View History'
]

use_cases_admin = [
    'Manage Users', 'Manage Inventory', 'Set Pricing', 'View Reports',
    'Process Refunds', 'Generate Analytics', 'System Config'
]

use_cases_external = [
    'Process Payment', 'Handle Refunds', 'Send Confirmations', 'Send Notifications'
]

# Customer use cases (left side)
for i, use_case in enumerate(use_cases_customer):
    y_pos = 9 - i * 0.8
    if y_pos > 1.5:  # Only draw if within system boundary
        ellipse = patches.Ellipse((3, y_pos), 2, 0.6, 
                                facecolor='lightyellow', 
                                edgecolor='black', 
                                linewidth=1)
        ax.add_patch(ellipse)
        ax.text(3, y_pos, use_case, fontsize=8, ha='center', va='center')

# Admin use cases (right side)
for i, use_case in enumerate(use_cases_admin):
    y_pos = 9 - i * 0.8
    if y_pos > 1.5:  # Only draw if within system boundary
        ellipse = patches.Ellipse((13, y_pos), 2, 0.6, 
                                facecolor='lightyellow', 
                                edgecolor='black', 
                                linewidth=1)
        ax.add_patch(ellipse)
        ax.text(13, y_pos, use_case, fontsize=8, ha='center', va='center')

# External use cases (bottom)
for i, use_case in enumerate(use_cases_external):
    x_pos = 2 + i * 3
    if x_pos < 14:  # Only draw if within system boundary
        ellipse = patches.Ellipse((x_pos, 2), 2, 0.6, 
                                facecolor='lightgreen', 
                                edgecolor='black', 
                                linewidth=1)
        ax.add_patch(ellipse)
        ax.text(x_pos, 2, use_case, fontsize=8, ha='center', va='center')

# Add some connection lines (simplified)
# Customer to use cases
for i in range(min(6, len(use_cases_customer))):
    y_pos = 9 - i * 0.8
    if y_pos > 1.5:
        ax.plot([1, 2], [8, y_pos], 'k-', linewidth=1, alpha=0.5)

# Admin to use cases
for i in range(min(6, len(use_cases_admin))):
    y_pos = 9 - i * 0.8
    if y_pos > 1.5:
        ax.plot([15, 12], [8, y_pos], 'k-', linewidth=1, alpha=0.5)

# External systems to use cases
ax.plot([1, 2], [4, 2], 'k-', linewidth=1, alpha=0.5)
ax.plot([15, 14], [4, 2], 'k-', linewidth=1, alpha=0.5)

# Legend
legend_elements = [
    patches.Patch(color='lightblue', label='System Boundary'),
    patches.Patch(color='lightyellow', label='Use Cases'),
    patches.Patch(color='lightgreen', label='External Use Cases')
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0.02, 0.98))

# Save the diagram
plt.tight_layout()
plt.savefig('alx-booking-uc.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
plt.close()

print("Use case diagram saved as 'alx-booking-uc.png'") 