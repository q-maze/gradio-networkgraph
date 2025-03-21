<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type { SelectData } from "@gradio/utils";

	import Network from "./Network.svelte";

	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value: { [key: string]: number };
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		select: SelectData;
		input: never;
		clear_status: LoadingStatus;
	}>;
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
			on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
		/>
	{/if}
	<Network
		gradio={gradio}
		value={value}
	/>
</Block>
