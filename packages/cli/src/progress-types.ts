import type {AggregateRenderProgress} from '@remotion/studio';

export const initialAggregateRenderProgress = (): AggregateRenderProgress => ({
	rendering: null,
	downloads: [],
	stitching: null,
	bundling: {
		progress: 0,
		doneIn: null,
	},
	copyingState: {
		bytes: 0,
		doneIn: null,
	},
});
